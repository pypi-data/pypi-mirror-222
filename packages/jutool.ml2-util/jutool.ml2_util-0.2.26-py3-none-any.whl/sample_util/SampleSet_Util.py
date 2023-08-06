from code_util.log import process_bar_iter
from sample_util.SampleSet import SampleSet
from sample_util.NLSampleSource import NLSampleSourceBase
from code_util.buffer import buffer_item


def splitset_by_labeltype_average(samplesource: NLSampleSourceBase, ori_set_name: str, get_label_type_func,
                                  set_count_dic: {}):
    """
    切分某个数据集，按照label进行平衡，并按照数量划分到不同的子set中，
    :param samplesource: 数据源
    :param ori_set_name: 需要进行切分的set
    :param get_label_type_func: 标识label的func回调，返回每条数据的lebel（均分依据）
    :param set_count_dic: 一个dic，表征需要划分不同子数据集的数量列表
    :return: 返回每个label的数量
    """
    label_type_dic = {}

    meta_data = samplesource.get_metadata_keys(ori_set_name)

    max_count_of_all_set = 0

    for new_set in set_count_dic.keys():
        samplesource.create_new_set(f"{ori_set_name}_{new_set}", f"split from {ori_set_name}", ["split"],
                                    meta_data['label_keys'], ori_set_name)
        max_count_of_all_set += set_count_dic[new_set]

    for item in SampleSet(samplesource, ori_set_name).shuffle():
        lable = get_label_type_func(item)
        if lable is None:
            continue
        if lable not in label_type_dic:
            label_type_dic[lable] = []
        if len(label_type_dic[lable]) > max_count_of_all_set:
            continue
        label_type_dic[lable].append(item)

    pointers = [(x, 0) for x in label_type_dic.keys()]
    index_pointer = 0
    for new_set in set_count_dic.keys():
        name = f"{ori_set_name}_{new_set}"
        counter = 0
        while True:
            point_data = pointers[index_pointer]

            if point_data[1] < len(label_type_dic[point_data[0]]):
                newdata = label_type_dic[point_data[0]][point_data[1]]
                newdata = [newdata[key] for key in meta_data['label_keys']]
                samplesource.add_row(name, newdata)
                counter += 1
                # add pointer
                pointers[index_pointer] = (point_data[0], point_data[1] + 1)
            if counter == set_count_dic[new_set]:
                break
            index_pointer += 1
            if index_pointer >= len(label_type_dic.keys()):
                index_pointer = 0
    samplesource.flush()

    return [key for key in label_type_dic.keys()]


def CopySet(samplesource: NLSampleSourceBase, ori_set_name: str, new_samplesource: NLSampleSourceBase, new_name: str,
            new_description: str, new_tags: [str], new_lables: [str]):
    """
    遍历复制一个set，用于重新命名、修改metadata等信息
    :param samplesource: 原始数据源
    :param ori_set_name: 原始set名称
    :param new_samplesource: 新数据源
    :param new_name: 新的set名称
    :param new_description: 新的描述
    :param new_tags: 新的tag信息
    :param new_lables: 新的lable信息
    :return: 无返回
    """
    new_samplesource.create_new_set(new_name, new_description, new_tags, new_lables)
    for item in process_bar_iter(SampleSet(samplesource, ori_set_name), f"Copy {ori_set_name} -> {new_name}"
            , samplesource.get_set_count(ori_set_name)):
        new_samplesource.add_row(new_name, item)


def Group_key_and_count(samplesource: NLSampleSourceBase, set_name: str, key: str):
    encode_dic = {}

    for item in SampleSet(samplesource, set_name):
        value = item[key]
        if value not in encode_dic:
            encode_dic[value] = 0
        encode_dic[value] += 1

    return encode_dic


def Group_SampleSet_Label_vocdic_to_buffer(samplesource: NLSampleSourceBase, set_name: str, key: str, buffer_key: str):
    """
    统计SampleSet中某个Label的数量，并生成互还字典，保存到buffer
    :param samplesource: sample数据源
    :param set_name: sampleset名称
    :param key: 需要统计的key
    :param buffer_key: 保存的buffer key
    :return: （dict，dict）正义字典和反义字典
    """
    encode_dic = {}
    decode_dic = {}
    index = 0

    for item in SampleSet(samplesource, set_name):
        value = item[key]
        if value not in encode_dic:
            encode_dic[value] = index
            decode_dic[index] = value
            index += 1

    buffer_item(buffer_key, (encode_dic, decode_dic))

    return encode_dic, decode_dic
