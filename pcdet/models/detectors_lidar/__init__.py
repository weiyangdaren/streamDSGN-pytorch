from .second_net import SECONDNet
from .voxel_rcnn import VoxelRCNN
from .centerpoint import CenterPoint
from .pointpillar import PointPillar
import torch.distributed as dist
from pcdet.utils.common_utils import create_logger

__all__ = {
    'SECONDNet': SECONDNet,
    'VoxelRCNN': VoxelRCNN,
    'CenterPoint': CenterPoint,
    'PointPillar': PointPillar,
}


def build_detector(model_cfg, num_class, dataset):
    model = __all__[model_cfg.NAME](
        model_cfg=model_cfg, num_class=num_class, dataset=dataset
    )

    try:
        logger = create_logger(rank=dist.get_rank())
    except:
        logger = create_logger()
    if hasattr(model_cfg, 'PRETRAINED_MODEL') and model_cfg.PRETRAINED_MODEL:
        model.load_params_from_file(
            filename=model_cfg.PRETRAINED_MODEL, to_cpu=True, logger=logger)

    return model
