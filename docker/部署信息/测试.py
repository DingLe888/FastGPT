import json
import re


def decode_base64_content(responseStr):

    # 步骤 1: 移除字符串中的无效控制字符，例如 '\uXXXX' 格式的字符
    # 这里我们使用正则表达式移除非打印字符
    cleaned_str = re.sub(r'[\u0000-\u001F\u007F-\u009F]', '', responseStr)

    # 步骤 2: 确保字符串中的双引号被正确转义
    cleaned_str = cleaned_str.replace('\\"', '\\\\\\"')

    # 步骤 3: 修复字符串格式，这里我们假设 responseStr 是多行字符串
    # 我们使用 triple-quoted 字符串来保持多行格式
    cleaned_str = f'''{cleaned_str}'''

    # 步骤 4: 检查并修复行尾字符，这里我们统一使用 '\n' 作为行尾
    cleaned_str = re.sub(r'\r\n|\r', '\n', cleaned_str)

    # 步骤 1: 替换单引号为双引号，因为 JSON 字符串应该使用双引号
    json_str = cleaned_str.replace('\'', '"').strip('"')

    # 步骤 2: 确保字符串中的所有反斜杠都被正确转义
    json_str = json_str.replace('\\\\', '\\\\\\\\')

    # 步骤 3: 修复 URL 中的反斜杠问题
    json_str = re.sub(r'(?<!:)\\(?=[^:/])', '/', json_str)

    # 尝试解析清理后的 JSON 字符串
    try:
        cc = json.loads(json_str)
        print("JSON 字符串解析成功!")
        # 接下来可以处理解析后的数据 cc
    except json.JSONDecodeError as e:
        print(f"解析 JSON 时发生错误: {e}")
    
def call_func(user_input):
    try:
        # 将 JSON 字符串转换成 Python 对象
        data = json.loads(user_input)
        
        # 初始化结果变量
        q_contents = []
        source_names = []
        
        # 检查 'choices' 和 'message' 键是否存在
        if "choices" in data and "message" in data["choices"][0]:
            message = data["choices"][0]["message"]
            # 检查 'content' 是否存在
            if "content" in message:
                # 解码 Base64 并尝试解析为 JSON
                content_json = json.loads(message["content"])
                if content_json is not None:
                    # 确保解析后的内容是列表
                    if isinstance(content_json, list):
                        for item in content_json:
                            # 提取 'q' 和 'sourceName' 并添加到结果列表中
                            if "q" in item:
                                q_contents.append(item["q"])
                            if "sourceName" in item:
                                source_names.append(item["sourceName"])
        
        # 拼接 'q' 内容
        q_concatenated = "    ----   ".join(q_contents)
        # 拼接 'sourceName' 内容
        source_names_concatenated = ",".join(source_names)
        
        # 打印结果
        print("Q Contents:")
        print(q_concatenated)
        print("\nSource Names:")
        print(source_names_concatenated)
        return {"q_contents": q_concatenated, "source_names": source_names_concatenated}
    
    except json.JSONDecodeError as e:
        return f"解析 JSON 时发生错误: {e}"
    except Exception as e:
        return f"处理 JSON 数据时发生未预料的错误: {e}"



responseStr = """
{"id": "", "model": "", "usage": {"prompt_tokens": 1, "completion_tokens": 1, "total_tokens": 1}, "choices": [{"message": {"role": "assistant", "content": "\n[\n {\n \"id\": \"666048b4b67a62ceaaab3056\",\n \"q\": \"## 5驱动器调试\\n### 步科调试\\n![表格 描述已自动生成](/api/system/img/666048afb67a62ceaaab2eef)\\n![C:Users\\\\陈卫东AppDataLocalTempWeChat Files\\\\aa21abfe72f264c5187d9cefc2331f0.jpg](/api/system/img/666048afb67a62ceaaab2ef1)将目标速度改成-400，此时能看到舵轮旋转至原点信号，远离电机的接近开关灯亮\\n![表格 描述已自动生成](/api/system/img/666048afb67a62ceaaab2ef3)\\n![C:Users\\\\陈卫东AppDataLocalTempWeChat Files\\\\e2a16cfa7c761930d8227fce0cf74d8.jpg](/api/system/img/666048afb67a62ceaaab2ef5)（4）修改原点参数\\n驱动器->控制模式->原点模式，设置原点偏移774400，原点模式26，原点转折信号速度450，原点信号速度1000，上电找原点1,。\\n点击驱动器->初始化/保存/重启，点击存储控制参数，存储电机参数，重启\\n![图形用户界面 中度可信度描述已自动生成](/api/system/img/666048afb67a62ceaaab2ef7)\",\n \"a\": \"\",\n \"chunkIndex\": 13,\n \"datasetId\": \"6660476db67a62ceaaab0997\",\n \"collectionId\": \"666048b2b67a62ceaaab2fbc\",\n \"sourceId\": \"666047a1b67a62ceaaab0d1f\",\n \"sourceName\": \"AGV调试文档 (2).docx\",\n \"score\": [\n {\n \"type\": \"embedding\",\n \"value\": 0.8930714130401611,\n \"index\": 0\n },\n {\n \"type\": \"rrf\",\n \"value\": 0.06557377049180328,\n \"index\": 0\n }\n ]\n },\n {\n \"id\": \"666048b4b67a62ceaaab3059\",\n \"q\": \"## 2修改激光头IP\\n### R200激光头\\n1.r2000雷达需要在雷达上进行操作\\n\\n如图r2000雷达前方两个按钮，更改ip操作需要使用这两个按钮进行\\n\\n![](/api/system/img/666048adb67a62ceaaab2eaf)2.点击选择按键进入ethernet setup\\n\\n![图片包含 室内, 小, 厨房, 冰箱 描述已自动生成](/api/system/img/666048adb67a62ceaaab2eb1)\\n\\n3.进入后点击下一个找到ip address进入\\n\\n![手里拿着枪 低可信度描述已自动生成](/api/system/img/666048adb67a62ceaaab2eb3)\\n\\n4.点击下一个按钮进行数字选择用来设置ip\\n\\n![图片包含 室内, 桌子, 厨房, 小 描述已自动生成](/api/system/img/666048adb67a62ceaaab2eb5)\\n\\n5.点击下一个进行子网掩码和网关的设置（设置IP注意设为同网段的ip比如车辆工控机为14.18.0.#那IP也设置为14.18.0.#）\",\n \"a\": \"\",\n \"chunkIndex\": 3,\n \"datasetId\": \"6660476db67a62ceaaab0997\",\n \"collectionId\": \"666048b2b67a62ceaaab2fbc\",\n \"sourceId\": \"666047a1b67a62ceaaab0d1f\",\n \"sourceName\": \"AGV调试文档 (2).docx\",\n \"score\": [\n {\n \"type\": \"embedding\",\n \"value\": 0.8930714130401611,\n \"index\": 1\n },\n {\n \"type\": \"rrf\",\n \"value\": 0.06451612903225806,\n \"index\": 1\n }\n ]\n },\n {\n \"id\": \"666048b4b67a62ceaaab305f\",\n \"q\": \"## 2修改激光头IP\\n### 欧蕾激光头\\n1.打开网络和internet\\n\\n![图形用户界面, 应用程序, Word 描述已自动生成](/api/system/img/666048adb67a62ceaaab2ea7)\\n\\n2.右键点击需要链接的网络点击属性打开后点击ipv4的属性界面进行配置\\n\\n3.前三位与需要配置的网络保持一致后一位选择不冲突的数字\\n\\n![图形用户界面, 文本, 应用程序 描述已自动生成](/api/system/img/666048adb67a62ceaaab2ea9)![图形用户界面, 文本 描述已自动生成](/api/system/img/666048adb67a62ceaaab2eab)\\n\\n4.欧镭激光头配置地址为192.168.1.100 使用网线与激光头进行连接\\n\\n5连接时关闭wifi使用网线网络，在浏览器输入192.168.1.100\\n\\n3进入配置界面，修改为192.168.0.110保存如图示进行修改\\n\\n![图形用户界面 中度可信度描述已自动生成](/api/system/img/666048adb67a62ceaaab2ead)\",\n \"a\": \"\",\n \"chunkIndex\": 2,\n \"datasetId\": \"6660476db67a62ceaaab0997\",\n \"collectionId\": \"666048b2b67a62ceaaab2fbc\",\n \"sourceId\": \"666047a1b67a62ceaaab0d1f\",\n \"sourceName\": \"AGV调试文档 (2).docx\",\n \"score\": [\n {\n \"type\": \"embedding\",\n \"value\": 0.8930714130401611,\n \"index\": 2\n },\n {\n \"type\": \"rrf\",\n \"value\": 0.06349206349206349,\n \"index\": 2\n }\n ]\n },\n {\n \"id\": \"666048b4b67a62ceaaab3062\",\n \"q\": \"## 5驱动器调试\\n### 步科调试\\n注意：如果限位开关是常开的，即轮子在中间位置（非限位位置）时，限位开关常亮；轮子在限位位置时灯灭。需要调整驱动器/控制模式/原点定义，修改原点开关为高电平，预设原点模式为24，并点击写入。点击存储控制参数，重启。\\n![48fce70d6af8b53241013a679bbe8d3](/api/system/img/666048afb67a62ceaaab2ef9)另，需要调整小车camel里面，监控/步科/极性改为2，加载配置生效。此时数字IO设置里面，正限位和原点信号，电平会取反。\\n![](/api/system/img/666048afb67a62ceaaab2efb)重启后，将工作模式改成1：位置模式。在控制字输入0080复位，0006去使能，000F使能，103F，舵轮会回到中间，既调试完成\\n![表格 描述已自动生成](/api/system/img/666048afb67a62ceaaab2efd)\\n![C:Users\\\\陈卫东AppDataLocalTempWeChat Files\\\\f7091e6c7de3fc9b0dc3e13c61a1230.jpg](/api/system/img/666048afb67a62ceaaab2eff)插上mcu网线，重启小车，监控看看mcu下发的工作模式为1：位置模式，控制字为103F，小车能正常回零位即调试完成。\",\n \"a\": \"\",\n \"chunkIndex\": 14,\n \"datasetId\": \"6660476db67a62ceaaab0997\",\n \"collectionId\": \"666048b2b67a62ceaaab2fbc\",\n \"sourceId\": \"666047a1b67a62ceaaab0d1f\",\n \"sourceName\": \"AGV调试文档 (2).docx\",\n \"score\": [\n {\n \"type\": \"embedding\",\n \"value\": 0.8930714130401611,\n \"index\": 3\n },\n {\n \"type\": \"rrf\",\n \"value\": 0.0625,\n \"index\": 3\n }\n ]\n },\n {\n \"id\": \"666048b4b67a62ceaaab306e\",\n \"q\": \"## 1修改IP\\n### 第一种方法\\n调试文档\\n\\n1、鼠标连接mcu板的usb口打开小车。\\n\\n![汽车的方向盘 描述已自动生成](/api/system/img/666048acb67a62ceaaab2e91)\\n\\n2、进入系统界面点击file syste\\n\\n![电脑的屏幕 描述已自动生成](/api/system/img/666048acb67a62ceaaab2e93)\\n\\n3、进入后点击etc\\n\\n![图片包含 图形用户界面 描述已自动生成](/api/system/img/666048acb67a62ceaaab2e95)\\n\\n4、进入network文件夹。\\n\\n![](/api/system/img/666048acb67a62ceaaab2e97)5、修改interfaces文件。\\n\\n![图形用户界面, 应用程序 描述已自动生成](/api/system/img/666048acb67a62ceaaab2e99)\\n\\n6、进入后对ip进行修改。\\n\\n![文本 描述已自动生成](/api/system/img/666048acb67a62ceaaab2e9b)\\n\\n7、有交换机的情况下修改完IP后下拉找到“auto eth1”和“iface eth1”然后把1改成0，修改完成后断电重启\\n\\n![文本, 信件 描述已自动生成](/api/system/img/666048acb67a62ceaaab2e9d)\",\n \"a\": \"\",\n \"chunkIndex\": 0,\n \"datasetId\": \"6660476db67a62ceaaab0997\",\n \"collectionId\": \"666048b2b67a62ceaaab2fbc\",\n \"sourceId\": \"666047a1b67a62ceaaab0d1f\",\n \"sourceName\": \"AGV调试文档 (2).docx\",\n \"score\": [\n {\n \"type\": \"embedding\",\n \"value\": 0.8930714130401611,\n \"index\": 4\n },\n {\n \"type\": \"rrf\",\n \"value\": 0.06153846153846154,\n \"index\": 4\n }\n ]\n }\n]"}, "finish_reason": "stop", "index": 0}]}
"""

decode_base64_content(responseStr)
