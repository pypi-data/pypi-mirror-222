from .jm_option import *


def download_album(jm_album_id, option=None):
    """
    下载一个本子集，入口api
    @param jm_album_id: 禁漫的本子的id，类型可以是str/int/iterable[str]。
    如果是iterable[str]，则会调用批量下载方法 download_album_batch
    @param option: 下载选项，为空默认是 JmOption.default()
    """

    if not isinstance(jm_album_id, (str, int)):
        return download_album_batch(jm_album_id, option)

    option, jm_client = build_client(option)
    album: JmAlbumDetail = jm_client.get_album_detail(jm_album_id)

    option.before_album(album)
    execute_by_condition(
        iter_objs=album,
        apply=lambda photo: download_by_photo_detail(photo, option),
        count_batch=option.decide_photo_batch_count(album)
    )
    option.after_album(album)


def download_photo(jm_photo_id, option=None):
    """
    下载一个本子的一章，入口api
    """
    option, jm_client = build_client(option)
    photo = jm_client.get_photo_detail(jm_photo_id)
    download_by_photo_detail(photo, option)


def download_by_photo_detail(photo: JmPhotoDetail, option=None):
    """
    下载一个本子的一章，根据 photo
    @param photo: 本子章节信息
    @param option: 选项
    """
    option, jm_client = build_client(option)

    # 下载准备
    use_cache = option.download_cache
    decode_image = option.download_image_decode
    jm_client.check_photo(photo)

    # 下载每个图片的函数
    def download_image(image: JmImageDetail):
        img_save_path = option.decide_image_filepath(image)
        image.is_exists = file_exists(img_save_path)

        option.before_image(image, img_save_path)
        if use_cache is True and image.is_exists:
            return
        jm_client.download_by_image_detail(
            image,
            img_save_path,
            decode_image=decode_image,
        )
        option.after_image(image, img_save_path)

    option.before_photo(photo)
    execute_by_condition(
        iter_objs=photo,
        apply=download_image,
        count_batch=option.decide_image_batch_count(photo)
    )
    option.before_photo(photo)


def download_album_batch(jm_album_id_iter: Union[Iterable, Generator],
                         option=None,
                         wait_finish=True,
                         ) -> List[Thread]:
    """
    批量下载album，每个album一个线程，使用的是同一个option。

    @param jm_album_id_iter: album_id的可迭代对象
    @param option: 下载选项，为空默认是 JmOption.default()
    @param wait_finish: 是否要等待这些下载线程全部完成
    @return 返回值是List[Thread]，里面是每个下载漫画的线程。
    """
    if option is None:
        option = JmOption.default()

    return thread_pool_executor(
        iter_objs=set(JmcomicText.parse_to_album_id(album_id) for album_id in jm_album_id_iter),
        apply_each_obj_func=lambda album_id: download_album(album_id, option),
        wait_finish=wait_finish,
    )


def execute_by_condition(iter_objs, apply: Callable, count_batch: int):
    """
    章节/图片的下载调度逻辑
    """
    count_real = len(iter_objs)

    if count_batch >= count_real:
        # 一个图/章节 对应 一个线程
        multi_thread_launcher(
            iter_objs=iter_objs,
            apply_each_obj_func=apply,
        )
    else:
        # 创建batch个线程的线程池
        thread_pool_executor(
            iter_objs=iter_objs,
            apply_each_obj_func=apply,
            max_workers=count_batch,
        )


def build_client(option: Optional[JmOption]) -> Tuple[JmOption, JmcomicClient]:
    """
    处理option的判空，并且创建jm_client
    """
    if option is None:
        option = JmOption.default()

    jm_client = option.build_jm_client()
    return option, jm_client


def create_option(filepath: str) -> JmOption:
    option = JmOption.from_file(filepath)
    return option
