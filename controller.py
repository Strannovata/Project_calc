import user_interface as user
import model_sum as model
import model_div 
import model_mult


def dutton_click():
    value_a = user.input_data()
    value_b = user.input_data()
    ####
    print('1 = div; 2 = mult; 3 = sum')
    print('выберите функцию: ')
    value_model = user.input_data()
    ####
    if value_model == 1: ###
        model.init(value_a, value_b)
        result = model.do_init()
        user.view_data(result)
    ###
    if value_model ==2:
        model_div.init(value_a, value_b)
        result = model_div.do_init() #
        user.view_data(result)
    ###
    if value_model == 3:
        model_mult.init(value_a, value_b)
        result = model_mult.do_init() #
        user.view_data(result)


### как то так если я правильно понял названия
