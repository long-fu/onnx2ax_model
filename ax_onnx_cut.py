import onnx
import sys

# v5s-face
# onnx.utils.extract_model("onnx/facedet.onnx", "onnx_cut/facedet.onnx", 
#                          ["input"], ["348",
#                                      "553",
#                                      "758"])

# scrfd face 
onnx.utils.extract_model("onnx/facedet_scrfd.onnx", "onnx_cut/facedet_scrfd.onnx", 
                         ["input.1"], ["524","523","526",
                                       "482","483", "485",
                                       "441","442","444"])

# onnx.utils.extract_model("onnx/facedet_scrfd.onnx", "onnx_cut/facedet_scrfd.onnx", 
#                          ["input.1"], ["539","530","547",
#                                        "489","498","506",
#                                        "448","457","465"])

# TODO: 后续转换
# resnet50
# onnx.utils.extract_model("onnx/facenet.onnx", "onnx_cut/facenet.onnx", 
#                          ["input"], ["/model.24/m.0/Conv_output_0",
#                                      "/model.24/m.1/Conv_output_0",
#                                      "/model.24/m.2/Conv_output_0"])

# v8s
# onnx.utils.extract_model("onnx/Detect.onnx", "onnx_cut/Detect.onnx", 
#                          ["images"], ["/model.24/m.0/Conv_output_0",
#                                      "/model.24/m.1/Conv_output_0",
#                                      "/model.24/m.2/Conv_output_0"])

## v8s-pose
# onnx.utils.extract_model("onnx/Pose.onnx", "onnx_cut/Pose.onnx", 
#                          ["images"], ["/model.22/Concat_1_output_0",
#                                      "/model.22/Concat_2_output_0",
#                                      "/model.22/Concat_3_output_0",
#                                      "/model.22/cv4.0/cv4.0.2/Conv_output_0",
#                                      "/model.22/cv4.1/cv4.1.2/Conv_output_0",
#                                      "/model.22/cv4.2/cv4.2.2/Conv_output_0"
#                                      ])

# onnx.utils.extract_model("onnx/yolov8s-pose.onnx", "onnx_cut/yolov8s-pose.onnx", 
#                          ["images"], ["/model.22/Concat_1_output_0",
#                                      "/model.22/Concat_2_output_0",
#                                      "/model.22/Concat_3_output_0",
#                                      "/model.22/cv4.0/cv4.0.2/Conv_output_0",
#                                      "/model.22/cv4.1/cv4.1.2/Conv_output_0",
#                                      "/model.22/cv4.2/cv4.2.2/Conv_output_0"
#                                      ])

# onnx.utils.extract_model("onnx/xxx.onnx", "onnx_cut/xxx.onnx", 
#                          ["images"], ["/model.31/m.0/Conv_output_0",
#                                      "/model.31/m.1/Conv_output_0",
#                                      "/model.31/m.2/Conv_output_0",
#                                      "/model.31/m.3/Conv_output_0"])



# onnx.utils.extract_model("onnx/xxx.onnx", "onnx_cut/xxx.onnx", 
#                          ["images"], ["/model.24/m.0/Conv_output_0",
#                                      "/model.24/m.1/Conv_output_0",
#                                      "/model.24/m.2/Conv_output_0"])

# onnx.utils.extract_model("onnx/BRH_phone.onnx", "onnx_cut/BRH_phone.onnx", 
#                          ["images"], ["/model.31/m.0/Conv_output_0",
#                                      "/model.31/m.1/Conv_output_0",
#                                      "/model.31/m.2/Conv_output_0",
#                                      "/model.31/m.3/Conv_output_0"])

# onnx.utils.extract_model("onnx/BRH_sign.onnx", "onnx_cut/BRH_sign.onnx", 
#                          ["images"], ["/model.24/m.0/Conv_output_0",
#                                      "/model.24/m.1/Conv_output_0",
#                                      "/model.24/m.2/Conv_output_0"])


