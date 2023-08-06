import abc, io, shutil
import os, pickle
from code_util.file import create_folder_if_not_exsited
from code_util.log import log_error, log, log_level_enum


class NLSampleSourceBase(metaclass=abc.ABCMeta):
    """
    数据存储源的基类，抽象类
    """

    @abc.abstractmethod
    def create_new_set(self, name: str, description: str, tags: [str], keys: [str], base_set="") -> bool:
        """
        创建新的数据set，抽象方法
        :param name: 新set的名称
        :param description: 新set的描述信息
        :param tags: 新set的tag信息
        :param keys: 新set的列名
        :param base_set: 父set的名称
        :return: 是否成功，bool类型返回
        """
        pass

    @abc.abstractmethod
    def has_set(self, name: str) -> bool:
        """
        此数据源中是否包含特定的数据set
        :param name: 需要查找的set名称
        :return: 结果bool类型的值
        """
        pass

    @abc.abstractmethod
    def add_row(self, name: str, data: []) -> bool:
        """
        添加新行
        :param name: 添加的目标set
        :param data: 列信息，list形式，顺序与set的列名顺序相同
        :return: 是否成功的bool返回
        """
        pass

    @abc.abstractmethod
    def get_metadata_keys(self, name: str) -> {}:
        """
        获得set的metadata信息，包括set的定义信息、数量等
        :param name: set名称
        :return: 字典类型的属性集合
        """
        pass

    @abc.abstractmethod
    def get_dir_list(self) -> {}:
        """
        获得当前源的所有set的列表信息
        :return: 字典类型的set集合
        """
        pass

    @abc.abstractmethod
    def iter_data(self, name: str):
        """
        遍历set中所有数据行
        :param name: set名称
        :return: 可迭代的数据对象，每个迭代是一行数据
        """
        pass

    @abc.abstractmethod
    def iter_pointer(self, name: str):
        """
        遍历返回set中所有行的指针信息
        :param name: set名称
        :return: 可迭代的指针对象
        """
        pass

    @abc.abstractmethod
    def delete_set(self, name: str):
        """
        删除特定的set
        :param name: 要删除的set名称
        :return: 无返回
        """
        pass

    @abc.abstractmethod
    def load_pointer_data(self, name: str, pointer):
        """
        通过特定的指针信息获得该指针信息的行
        :param name: set名称
        :param pointer: 指针信息
        :return: 该指针指向的行信息
        """
        pass

    @abc.abstractmethod
    def get_set_count(self, name: str):
        """
        获得set的数量
        :param name: set名称
        :return: 返回数量信息
        """
        pass

    @abc.abstractmethod
    def add_attachment(self, set_name: str, key, data):
        """
        向set添加特定的附加信息
        :param set_name: 添加的set
        :param key: 附加信息的key
        :param data: 附加信息
        :return: 无返回
        """
        pass

    @abc.abstractmethod
    def read_attachment(self, set_name: str):
        """
        读取set的附加信息
        :param set_name: 读取的set名称
        :return: 返回附加信息
        """
        pass

    @abc.abstractmethod
    def read_one_row(self, set_name: str):
        """
        读取set的第一行信息
        :param set_name: set名称
        :return: 第一行的数据
        """
        pass

    def arrange_dir_list(self, dir_list: {}):
        """
        构建基于树形目录的控制台输出
        :param dir_list: metadata列表，一般取自 get_metadata_keys
        :return: 返回树形字典，表示此数据源所有set的树形结构
        """
        new_dic = {key: {
            'meta': dir_list[key]['meta'],
            'children': {},
            'count': dir_list[key]['count'],
            'base_set': dir_list[key]['meta']['base_set']
        } for key in dir_list.keys()}

        for set_key in new_dic.keys():
            if new_dic[set_key]['base_set'] != "":
                if new_dic[set_key]['base_set'] not in new_dic:
                    log(f"没有找到{set_key}的父节点，置顶输出", log_level=log_level_enum.Warning)
                    new_dic[set_key]['base_set'] = ""
                else:
                    base_set_name = new_dic[set_key]['base_set']
                    new_dic[base_set_name]['children'][set_key] = new_dic[set_key]

        # if print:
        #     def printsub(level: int, name, item):
        #         blank_str = ""
        #         for _ in range(level):
        #             blank_str += "\t"
        #         print(f"{blank_str} - {name}({item['count']}): {item['meta']['des']}")
        #         for sub_item in item['children'].keys():
        #             printsub(level + 1, sub_item, item['children'][sub_item])
        #
        #     for key in new_dic.keys():
        #         printsub(0, key, new_dic[key])

        return {key: new_dic[key] for key in new_dic if new_dic[key]['base_set'] == ""}

    def print_markdown_arrange_dir_list(self, dir_list: {}, path=None, max_length=1000):
        """
        打印此数据源所有数据set的预览页（markdown）
        :param dir_list: metadata列表，一般取自 get_metadata_keys
        :param path: 输出目录
        :param max_length: 每行数据的最大现实长度
        :return:
        """
        local_path = path
        if local_path is None:
            local_path = "data_list.md"

        def doc_to_markdown(s):
            if not isinstance(s, str):
                return s
            alllines = s.split('\n')[:20]
            return "\n >".join(alllines)[:max_length]

        with open(local_path, "w") as file:
            lines = ["[toc]"]
            new_dic = {}
            files_order_list = sorted([k for k in dir_list.keys()], key=lambda item: len(item.split('_')))
            key_pointers = {}
            for set_key in files_order_list:
                row_key = dir_list[set_key]['meta']['label_keys']
                one_row = self.read_one_row(set_key)
                if dir_list[set_key]['meta']['base_set'] == "":
                    new_dic[set_key] = {
                        'meta': dir_list[set_key]['meta'],
                        'children': {},
                        'count': dir_list[set_key]['count'],
                        'row_sample': zip(row_key, one_row)
                    }
                    key_pointers[set_key] = new_dic[set_key]
                else:
                    base_set_name = dir_list[set_key]['meta']['base_set']
                    key_pointers[base_set_name]['children'][set_key] = {
                        'meta': dir_list[set_key]['meta'],
                        'children': {},
                        'count': dir_list[set_key]['count'],
                        'row_sample': zip(row_key, one_row)
                    }
                    key_pointers[set_key] = key_pointers[base_set_name]['children'][set_key]

            def printsub(level: int, name, item):
                blank_str = "#"
                for _ in range(level):
                    blank_str += "#"
                lines.append(f"{blank_str} {name}")
                lines.append(f"**{item['meta']['des']}**")
                lines.append(f"count: {item['count']}")
                for key, val in item['row_sample']:
                    new_val = doc_to_markdown(val)
                    lines.append(f"key: {key}")
                    lines.append(f"> {new_val}")
                    lines.append(" ")
                for sub_item in item['children'].keys():
                    printsub(level + 1, sub_item, item['children'][sub_item])

            for key in new_dic.keys():
                printsub(0, key, new_dic[key])

            file.writelines("\n".join(lines))

    def flush(self):
        """
        提交所有更改
        :return: 无返回
        """
        pass


class LocalDisk_NLSampleSource(NLSampleSourceBase):
    """
    本地磁盘的数据源.
    """

    def get_dir_list(self) -> {}:
        """
        获得当前源的所有set的列表信息
        :return: 字典类型的set集合
        """
        sets = [file for file in os.listdir(self.base_folder) if not file.startswith('.')]
        sets_infos = {}
        for p_set in sets:
            base_f = self._try_get_file_obj(p_set)
            file_index, append_seek, data_start_seek, count, filecount, current_count = self._read_base_header(base_f)
            node = self._read_node(base_f)
            sets_infos[p_set] = {
                'meta': node,
                'count': count,
                'filecount': filecount
            }
        return sets_infos

    def __init__(self, folder_path):
        """
        初始化数据源
        :param folder_path: 数据源存储的本地目录
        """
        self.base_folder = folder_path
        self.int_size = 8
        self.shortint_size = 4
        self.pointer_size = self.int_size + self.shortint_size
        self.header_node_size = 5 * 1024
        self.file_size = 1024 * 1024 * 100
        self.file_pool = {}

        self.base_seek_dic = {
            'file_index': 0,
            'append_seek': self.int_size,
            'data_start_seek': self.int_size + self.pointer_size,
            'data_count': self.int_size * 2 + self.pointer_size,
            'file_count': self.int_size * 3 + self.pointer_size,
            'current_file_count': self.int_size * 4 + self.pointer_size,
        }

        self.linked_seek_dic = {
            'file_index': 0,
            'current_file_count': self.int_size,
            'data_start_seek': self.int_size * 2,
        }

        create_folder_if_not_exsited(self.base_folder)

    def _try_get_file_obj(self, name: str, file_index=0):
        set_name = name
        if file_index != 0:
            name = f"{name}__{file_index}"
        if name not in self.file_pool:
            self.file_pool[name] = open(os.path.join(self.base_folder, set_name, f"{name}.dlib"), 'rb+')

        return self.file_pool[name]

    def __del__(self):
        """
        提交所有打开的文档更改并关闭
        :return:
        """
        for name in self.file_pool.keys():
            self.file_pool[name].close()

    def flush(self):
        """
        提交所有的更改
        :return: 无返回
        """
        for name in self.file_pool.keys():
            self.file_pool[name].flush()

    def _read_int(self, f) -> int:
        return int.from_bytes(f.read(self.int_size), "big", signed=False)

    def _write_int(self, f, int_value: int):
        f.write(int_value.to_bytes(self.int_size, "big", signed=False))

    def _add_int_plusone(self, f, seekp):
        f.seek(seekp)
        v = self._read_int(f)
        v += 1
        f.seek(seekp)
        self._write_int(f, v)

    def _read_shortint(self, f) -> int:
        return int.from_bytes(f.read(self.shortint_size), "big", signed=False)

    def _write_shortint(self, f, int_value: int):
        f.write(int_value.to_bytes(self.shortint_size, "big", signed=False))

    def _read_pointer(self, f) -> (int, int):
        p = self._read_shortint(f)
        s = self._read_int(f)
        return (p, s)

    def _write_pointer(self, f, page: int, seek: int):
        self._write_shortint(f, page)
        self._write_int(f, seek)

    def _read_node(self, f):
        f_len = self._read_int(f)
        act_len = self._read_int(f)
        with io.BytesIO() as bf:
            bf.write(f.read(act_len))
            bf.seek(0)
            return pickle.load(bf)

    def _seek_to_node(self, f):
        o_loc = f.tell()
        f_len = self._read_int(f)
        act_len = self._read_int(f)
        c_loc = f.tell()
        f.seek(c_loc + act_len)
        return o_loc

    def _write_node(self, f, node, size=None):
        """
        Node format:  plan_size(int),Act_size(int), data
        :param f:
        :param node:
        :param size:
        :return:
        """
        with io.BytesIO() as bf:
            pickle.dump(node, bf)
            act_len = bf.tell()
            if size and act_len > size:
                log_error("超过Node限制")
            f_len = act_len if size is None else size
            bf.seek(0)
            self._write_int(f, f_len)
            self._write_int(f, act_len)
            f.write(bf.read(act_len))

    def _read_base_header(self, f):
        f.seek(0)
        file_index = self._read_int(f)
        append_seek = self._read_pointer(f)
        data_start_seek = self._read_int(f)
        count = self._read_int(f)
        file_count = self._read_int(f)
        current_file_count = self._read_int(f)
        # node = self._read_node(f)
        return file_index, append_seek, data_start_seek, count, file_count, current_file_count

    def _read_linked_header(self, f):
        f.seek(0)
        file_index = self._read_int(f)
        current_count = self._read_int(f)
        data_start_seek = self._read_int(f)

        return file_index, current_count, data_start_seek

    def load_pointer_data(self, name: str, pointer):
        file_index, start_seek_location = pointer
        c_f = self._try_get_file_obj(name, file_index)
        c_f.seek(start_seek_location)
        return self._read_node(c_f)

    def create_new_set(self, name: str, description: str, tags: [str], keys: [str],
                       base_set="") -> bool:
        """
        header format:  file_index(int): 文件序号
                        append_seek(pointer): 添加新数据指针
                        data_start_seek(int): 本文件中数据的开始位置
                        data_count(int): 数据的个数
                        file_count(int): 文件链个数
                        current_file_count(int): 当前数据数量
                        header_node: 数据
        :param name:
        :param description:
        :param tags:
        :param label_keys:
        :return:
        """
        # if '_' in name:
        #     log_error("set名中不能包含符号 '_' ")

        # if base_set != "":
        #     name = f"{base_set}_{name}"

        os.mkdir(os.path.join(self.base_folder, name))
        with open(os.path.join(self.base_folder, name, f"{name}.dlib"), 'wb') as f:
            header = {
                'name': name,
                'des': description,
                'tags': tags,
                'label_keys': keys,
                'base_set': base_set,
                'base_set_process': ""
            }
            self._write_int(f, 0)  # file_index
            start_seek = self.int_size * 5 + self.pointer_size + self.header_node_size
            self._write_pointer(f, 0, start_seek)  # append_seek
            self._write_int(f, start_seek)  # data_start_seek
            self._write_int(f, 0)  # data_count
            self._write_int(f, 1)  # file_count
            self._write_int(f, 0)  # current_file_count
            self._write_node(f, header, self.header_node_size)

        return True

    def has_set(self, name: str) -> bool:
        if os.path.exists(os.path.join(self.base_folder, name, f"{name}.dlib")):
            return True
        return False

    def add_row(self, name: str, data: []) -> bool:
        if not isinstance(data, list):
            log_error("数据格式错误")

        base_f = self._try_get_file_obj(name)
        file_index, append_seek, data_start_seek, count, filecount, current_count = self._read_base_header(base_f)

        meta_data_keys = self._read_node(base_f)['label_keys']
        assert len(data) == len(meta_data_keys)

        f = self._try_get_file_obj(name, append_seek[0])

        f.seek(append_seek[1])
        self._write_node(f, data)
        new_append_seek = f.tell()
        new_append_page = append_seek[0]

        if new_append_seek > self.file_size:
            new_append_page += 1
            with open(os.path.join(self.base_folder, name, f"{name}__{new_append_page}.dlib"), 'wb') as f_new:
                self._write_int(f_new, new_append_page)
                self._write_int(f_new, 0)
                self._write_int(f_new, 3 * self.int_size)
                new_append_seek = f_new.tell()
            self._add_int_plusone(base_f, self.base_seek_dic['file_count'])  # file_count

        base_f.seek(self.base_seek_dic['append_seek'])
        self._write_pointer(base_f, new_append_page, new_append_seek)  # append_seek

        self._add_int_plusone(base_f, self.base_seek_dic['data_count'])  # data_count

        # updata current file count
        if append_seek[0] == 0:
            self._add_int_plusone(f, self.base_seek_dic['current_file_count'])
        else:
            self._add_int_plusone(f, self.linked_seek_dic['current_file_count'])

        return True

    def iter_data(self, name: str):
        base_f = self._try_get_file_obj(name)
        file_index, append_seek, data_start_seek, count, filecount, current_count = self._read_base_header(base_f)

        for file_index in range(filecount):
            c_f = self._try_get_file_obj(name, file_index)
            if file_index == 0:
                c_f.seek(self.base_seek_dic['current_file_count'])
            else:
                c_f.seek(self.linked_seek_dic['current_file_count'])
            count = self._read_int(c_f)

            if file_index == 0:
                c_f.seek(self.base_seek_dic['data_start_seek'])
            else:
                c_f.seek(self.linked_seek_dic['data_start_seek'])
            start_seek_location = self._read_int(c_f)
            c_f.seek(start_seek_location)
            for f_count in range(count):
                yield self._read_node(c_f)

    def read_one_row(self, name: str):
        base_f = self._try_get_file_obj(name)
        file_index, append_seek, data_start_seek, count, filecount, current_count = self._read_base_header(base_f)

        c_f = self._try_get_file_obj(name, 0)
        c_f.seek(self.base_seek_dic['current_file_count'])
        count = self._read_int(c_f)

        c_f.seek(self.base_seek_dic['data_start_seek'])

        start_seek_location = self._read_int(c_f)
        c_f.seek(start_seek_location)
        return self._read_node(c_f)

    def iter_pointer(self, name: str):
        base_f = self._try_get_file_obj(name)
        file_index, append_seek, data_start_seek, count, filecount, current_count = self._read_base_header(base_f)

        for file_index in range(filecount):
            c_f = self._try_get_file_obj(name, file_index)
            if file_index == 0:
                c_f.seek(self.base_seek_dic['current_file_count'])
            else:
                c_f.seek(self.linked_seek_dic['current_file_count'])
            count = self._read_int(c_f)

            if file_index == 0:
                c_f.seek(self.base_seek_dic['data_start_seek'])
            else:
                c_f.seek(self.linked_seek_dic['data_start_seek'])
            start_seek_location = self._read_int(c_f)
            c_f.seek(start_seek_location)
            for f_count in range(count):
                yield (file_index, self._seek_to_node(c_f))

    def get_set_count(self, name: str):
        base_f = self._try_get_file_obj(name)
        file_index, append_seek, data_start_seek, count, filecount, current_count = self._read_base_header(base_f)
        return count

    def get_metadata_keys(self, name: str) -> {}:
        base_f = self._try_get_file_obj(name)
        file_index, append_seek, data_start_seek, count, filecount, current_count = self._read_base_header(base_f)
        return self._read_node(base_f)

    def print_set_info(self, name: str):
        """
        在控制台打印某个set的信息
        :param name: set的名称
        :return: 无返回
        """
        base_f = self._try_get_file_obj(name)
        v_count = 0
        file_index, append_seek, data_start_seek, count, filecount, current_count = self._read_base_header(base_f)
        print("*************************************************************** ")
        print(f"file_index(int):{file_index} \t append_seek:{append_seek[0]},{append_seek[1]} ")
        print(f"data_start_seek(int):{data_start_seek} \t count(int):{count} ")
        print(f"filecount(int):{filecount} \t current_count(int):{current_count} ")
        v_count += current_count
        for index in range(1, filecount):
            cn_f = self._try_get_file_obj(name, index)
            file_index, current_count, start_append_seek = self._read_linked_header(cn_f)
            v_count += current_count
            print("———————————————————————————————————————————————————————————————— ")
            print(
                f"file_index(int):{file_index} \t current_count:{current_count},start_append_seek : {start_append_seek} ")
        if v_count != count:
            print(f'Count_ERROR:{count}->{v_count}')
        print("*************************************************************** ")

    def delete_set(self, name: str):
        for kname in self.file_pool.keys():
            self.file_pool[kname].close()
        self.file_pool = {}
        shutil.rmtree(os.path.join(self.base_folder, name))

    def add_attachment(self, set_name: str, key, data):
        if not self.has_set(set_name):
            log_error("没有此set")

        attachment_file_path = os.path.join(self.base_folder, set_name, f"{set_name}.attch")
        if not os.path.exists(attachment_file_path):
            with open(attachment_file_path, 'wb') as f:
                self._write_int(f, 0)
                self._write_int(f, self.int_size * 2)

        with open(attachment_file_path, 'rb+') as f:
            count = self._read_int(f)
            start_loc = self._read_int(f)
            f.seek(start_loc)
            self._write_node(f, {'key': key, 'data': data})
            next_start = f.tell()
            f.seek(0)
            self._write_int(f, count + 1)
            self._write_int(f, next_start)

    def read_attachment(self, set_name: str):
        attachment_file_path = os.path.join(self.base_folder, set_name, f"{set_name}.attch")
        if not os.path.exists(attachment_file_path):
            log_error("此set没有附件")

        attach_dic = []
        with open(attachment_file_path, 'rb+') as f:
            count = self._read_int(f)
            start_loc = self._read_int(f)
            for _ in range(count):
                attach_dic.append(self._read_node(f))

        return attach_dic


class Memory_NLSampleSource(NLSampleSourceBase):
    """
    构建一个基于内存的SampleSource
    """

    def __init__(self):
        self.datas = {}

    def create_new_set(self, name: str, description: str, tags: [str], keys: [str], base_set="",
                       base_set_process="") -> bool:
        if name in self.datas:
            log_error("已存在相同的set")

        self.datas[name] = {
            'name': name,
            'des': description,
            'tags': tags,
            'label_keys': keys,
            'base_set': base_set,
            'base_set_process': base_set_process,
            'data': [],
        }

        return True

    def has_set(self, name: str) -> bool:
        return name in self.datas

    def add_row(self, name: str, data: []) -> bool:
        self.datas[name]['data'].append(data)
        return True

    def get_metadata_keys(self, name: str) -> {}:
        return {
            'des': self.datas[name]['des'],
            'tags': self.datas[name]['tags'],
            'label_keys': self.datas[name]['label_keys'],
            'base_set': self.datas[name]['base_set'],
            'base_set_process': self.datas[name]['base_set_process'],
        }

    def get_dir_list(self) -> {}:
        # 'meta': node,
        # 'count': count,
        # 'filecount': filecount
        return {x_key: {
            'meta': self.get_metadata_keys(x_key),
            'count': self.get_set_count(x_key),
        }
            for x_key in self.datas.keys()}

    def iter_data(self, name: str):
        for item in self.datas[name]['data']:
            yield item

    def iter_pointer(self, name: str):
        for idx in range(len(self.datas[name]['data'])):
            yield idx

    def delete_set(self, name: str):
        del self.datas[name]

    def load_pointer_data(self, name: str, pointer):
        return self.datas[name]['data'][pointer]

    def get_set_count(self, name: str):
        return len(self.datas[name]['data'])

    def add_attachment(self, set_name: str, key, data):
        log_error("not support")

    def read_attachment(self, set_name: str):
        log_error("not support")

    def read_one_row(self, set_name: str):
        return self.datas[set_name]['data'][0]
