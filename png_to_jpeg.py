import os
import cv2


# Run my script for specific file
def png_to_jpeg(path):
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            name = file.split('.')[0]
            path1 = f'{path}/{file}'
            depth = len(name[:-3])
            image = cv2.imread(path1)
            if image is None:
                print('No such file!')
            else:
                if not os.path.exists(path + f'/{name[:depth]}'):
                    os.mkdir(path + f'/{name[:depth]}')
                cv2.imwrite(os.path.normpath(f'{path}/{file[:depth]}/{name}.jpeg'), image)
                pass


def png_to_jpeg_main(path):
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            name = file.split('.')[0]
            path1 = f'{path}/{file}'
            image = cv2.imread(path1)
            if image is None:
                raise NameError
            else:
                cv2.imwrite(os.path.normpath(f'{path}/{name}.jpeg'), image)


if __name__ == '__main__':

    not_over = True
    print('Choose method: '
          'normal directory (1)'
          'specific directory (2)'
          'Note: specific directory sort files with almost same name to one directory'
          'Example files "01.02.2021(1).png", "01.02.2021(2).png" --> /01.02.2021/[01.02.2021(1).png,01.02.2021(2).png]')
    method = input('Your choise is: 1, 2 ? ')
    if ' ' in method:
        method.replace(' ', '')
    while not_over:
        path = input('Put /PATH/HERE/: ')
        if path == '':
            not_over = False
            continue
        try:
            if method == '2':
                png_to_jpeg(os.path.normpath(path))
            else:
                png_to_jpeg_main(os.path.normpath(path))
        except Exception as exc:
            for dirpath, dirnames, filenames in os.walk(path):
                print(dirnames)
            print('Ooops something going wrong', exc)
