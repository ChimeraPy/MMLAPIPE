import logging.config

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "standard": {
            "format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "formatter": "standard",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",  # Default is stderr
        }
    },
    "loggers": {
        "c2mmla": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": True,
        }
    },
}

# Setup the logging configuration
logging.config.dictConfig(LOGGING_CONFIG)

from .kinect_node import KinectNode
from .yolo_node import YOLONode
from .generic_nodes.video_nodes import ShowWindows
from .generic_nodes.video_nodes import Video
from .mf_sort.detector import MFSortDetector
from .mf_sort.bbox_painter import BBoxPainter
