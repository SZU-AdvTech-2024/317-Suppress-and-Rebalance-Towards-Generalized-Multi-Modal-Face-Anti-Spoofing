from models.my_adapter import MMDG


def get_model(model_name, args=None):
    model_dict = {
        "mmdg": get_MMDG
    }
    return model_dict[model_name](args)


def get_MMDG():
    return MMDG()