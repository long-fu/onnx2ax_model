#!/bin/bash

# yolov5face
# pulsar2 build --input onnx_cut/facedet.onnx --output_dir weights/facedets \
#     --config config/yolov5s_face_yuv_config.json

# scrfd face
pulsar2 build --input onnx_cut/facedet_scrfd_new.onnx --output_dir weights/facedets_scrfd \
    --config config/scrfd_face_yuv_config.json

# pulsar2 build --input onnx_cut/xxxxx.onnx --output_dir weights/xxxxx \
#     --config config/resnet50_yuv_config.json    

# pulsar2 build --input onnx_cut/xxxx.onnx --output_dir weights/xxxx \
#     --config config/yolov5s_yuv_config_3head.json

# # v8\5 
# pulsar2 build --input onnx_cut/Detect.onnx --output_dir weights/Detect \
#     --config config/yolov5s_yuv_config_3head.json

# # v8 post
# pulsar2 build --input onnx_cut/Pose.onnx --output_dir weights/Pose \
#     --config config/yolov8s_pose_yuv_config.json

# pulsar2 build --input onnx_cut/yolov8s-pose.onnx --output_dir weights/yolov8s_pose \
#     --config config/yolov8s_pose_yuv_config.json

# pulsar2 build --input onnx_cut/xxxxx.onnx --output_dir weights/xxxxx \
#     --config config/yolov5s_yuv_config_3head.json

# pulsar2 build --input onnx_cut/xxxxxx.onnx --output_dir weights/xxxxxx \
#     --config config/yolov5s_yuv_config_4head.json
