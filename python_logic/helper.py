
class Helper(object):
    @staticmethod
    def change_selected_options(data_structure, selected_value):
        for index in range(len(data_structure)):
            if data_structure[index]['value'] == selected_value:
                data_structure[index]['selected'] = "yes"
            else:
                data_structure[index]['selected'] = "no"

        return data_structure

