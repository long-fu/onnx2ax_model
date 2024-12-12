import onnx
def change_input_output_dim(model):
    # Use some symbolic name not used for any other dimension
    sym_batch_dim = "batch"

    # The following code changes the first dimension of every input to be batch-dim
    # Modify as appropriate ... note that this requires all inputs to
    # have the same batch_dim 
    inputs = model.graph.input
    for input in inputs:
        # Checks omitted.This assumes that all inputs are tensors and have a shape with first dim.
        # Add checks as needed.
        dim1 = input.type.tensor_type.shape.dim[0]
        # update dim to be a symbolic value
        dim1.dim_param = sym_batch_dim
        # or update it to be an actual value:
        # dim1.dim_value = actual_batch_dim
    
    outputs = model.graph.output
    for output in outputs:
        # Checks omitted.This assumes that all inputs are tensors and have a shape with first dim.
        # Add checks as needed.
        dim1 = output.type.tensor_type.shape.dim[0]
        # update dim to be a symbolic value
        dim1.dim_param = sym_batch_dim

def change_input_node_name(model, input_names):
    for i,input in enumerate(model.graph.input):
        input_name = input_names[i]
        for node in model.graph.node:
            for i, name in enumerate(node.input):
                if name == input.name:
                    node.input[i] = input_name
        input.name = input_name
        

def change_output_node_name(model, output_names):
    for i,output in enumerate(model.graph.output):
        output_name = output_names[i]
        
        for node in model.graph.node:
            for i, name in enumerate(node.output):
                if name == output.name:
                    print("out name ori: ", output.name, " -> ", output_name)
                    node.output[i] = output_name
        output.name = output_name


onnx_path = "onnx_cut/ALL_facedet_scrfd.onnx"
save_path = "onnx_cut/ALL_facedet_scrfd_new.onnx"
model = onnx.load(onnx_path)  
# change_input_output_dim(model) ##改成动态batch
change_input_node_name(model, ["input"])  ##改输入节点名称
change_output_node_name(model, ["bbox_32", "score_32","kps_32",
                                "score_16", "bbox_16","kps_16",
                                "score_8","bbox_8","kps_8"])  ##改输出节点名称

onnx.save(model, save_path)
