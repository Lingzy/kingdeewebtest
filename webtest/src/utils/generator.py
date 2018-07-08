import random
from faker import Factory,Faker

# fake = Factory().create('zh_CN')
fake = Faker('zh_CN')


def random_phone_number():
    # 随机电话号码
    return fake.phone_number()


def random_name():
    # 随机姓名
    return fake.name()


def random_address():
    return fake.address()


def random_email():
    return fake.email()


def random_ipv4():
    return fake.ipv4()


def random_str(min_chars=0,max_chars=8):
    return fake.pystr(min_chars=min_chars,max_chars=max_chars)

def factory_generate_ids(starting_id=1, increment=1):
    # 返回一个生成器函数，调用这个函数产生生成器，从start_id开始，步长为icrement
    def generate_start_ids():
        val = starting_id
        local_increment = increment
        while True:
            yield val
            val += local_increment
    return generate_start_ids

def factory_choice_generator(values):
    """返回一个生成器函数，调用这个函数产生生成器，从给定的list中随机取一项"""
    def choice_generator():
        my_list = list(values)
        while True:
            yield random.choice(my_list)
    return choice_generator


if __name__ == '__main__':
    print(random_address())
    print(random_email())
    print(random_phone_number())
    print(random_ipv4())
    print(random_str())
    print(random_name())
    id_gen = factory_generate_ids(starting_id=0,increment=2)()
    for i in range(5):
        print(next(id_gen))

    choices = ['john','sam','jli','rose']
    choice_gen = factory_choice_generator(choices)()
    for i in range(5):
        print(next(choice_gen))
