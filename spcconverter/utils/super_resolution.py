from ..utils.call_inf_server import call_inf_server


def super_resolution(image):
    print(f"[{__name__}]start")
    sres_image = call_inf_server("super_resolution", image)
    print(f"[{__name__}]end")
    return sres_image
