from typing import Optional


def R(mapper_class):
    def get(id: Optional[int] = None, page_num: Optional[int] = None, page_size: Optional[int] = None, **kwargs):
        if id:
            return mapper_class.get_json(id)
        else:
            return mapper_class.get_jsons(page_num=page_num, page_size=page_size)

    def post(data: dict, id: Optional[int] = None):
        if id:
            mapper_class.save(id, data)
        else:
            mapper_class.add(data)

    def delete(id: int):
        mapper_class.delete(id=id)

    method_dict = {
        'get': get,
        'post': post,
        'delete': delete
    }

    return type('Resource', (object,), method_dict)
    
