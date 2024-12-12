import onnx
import sys


def main(args):
    # print("参数个数",len(args), args[0], args[1])
    # return
    if len(args) < 2:
        print('请输入参数需要转换的模型')
        return    
    # 加载ONNX模型
    model_path = args[1]  # 替换为你的ONNX模型文件路径
    model = onnx.load(model_path)    
   # 打印网络结构
    # print("Model Structure:")
    # print(model)

    # 打印输入信息
    # print("name:", args[1], "Inputs:")
    for input in model.graph.input:
        # print(input.name, end=': ')
        shape = [dim.dim_value for dim in input.type.tensor_type.shape.dim]
        # print(shape)
        print("name:", args[1], "Inputs:", input.name, ": ", shape)
    
    # 打印输出信息
    # print("\nOutputs:")
    # for output in model.graph.output:
    #     print(output.name, end=': ')
    #     shape = [dim.dim_value for dim in output.type.tensor_type.shape.dim]
    #     print(shape)     

if __name__ == '__main__':
    
    main(sys.argv)