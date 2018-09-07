import json
def retrieve_error_case(id_pred_path, dev_path, out_put_path):

    '''
    get a more readable error case file
    :param id_pred_path: error case data, each line like query_id:predict_answer
    :param dev_path:  dev data, each line is a json , like {'query_id': id, 'passage':passage', ...}
    :param out_put_path: error case data which is more convenient for checking
    '''
    dev_data = {}
    with open(dev_path, 'r',encoding='utf-8') as f:
        for line in f:
            row = json.loads(line)
            if row['query_id'] not in dev_data:
                dev_data[row['query_id']] = {'id':row['query_id'],
                                             'query':row['query'],
                                             'passage':row['passage'],
                                             'answer':row['answer']}
            else:
                raise Exception('repeated query id({0}) occurs, please check original data'.format(row['query_id']))
    error_cases = []
    with open(id_pred_path, 'r', encoding = 'utf-8') as f:
        for line in f:
            row = line.strip().split(':')
            if int(row[0]) in dev_data:
                case = dev_data[int(row[0])]
                case.update({'predict': row[1]})
                error_cases.append(case)
            else:
                raise Exception('id({0}) not in original data, but found in error_case_id_answer file'.format(row[0]))
    with open(out_put_path, 'w+',encoding='utf-8') as f:
        for case in error_cases:
            f.write(str(case))
            f.write('\n')
    print('retrieve error case finish, save data at {0}'.format(out_put_path))

retrieve_error_case("E:/Python/writeexl/error_case_id_backup.txt","E:/Python/writeexl/ai_challenger_oqmrc_validationset.json","E:/Python/writeexl/error.txt")