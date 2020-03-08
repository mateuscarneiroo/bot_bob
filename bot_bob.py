#-*- coding: utf-8 -*-

#Importação do web
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#importação do machine learning e bot
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

import os
import time
import random

bot = ChatBot('bot_bob')
trainer = ListTrainer(bot)
driver = webdriver.Chrome(ChromeDriverManager().install()) #instalação do webdriver(chrome)
driver.get('http://web.whatsapp.com')
driver.maximize_window()

#Localizando o arquivo a ser lido com as conversas e salvando as linhas em uma variavel
for treino in os.listdir("C:\\Users\\NOME DO DIRETÓRIO\\dicionarios"):
        if (treino == "frases.txt"):
            frases_f = open("C:\\Users\\NOME DO DIRETÓRIO\\dicionarios" +'\\'+treino, 'r', encoding='utf-8').readlines()
            trainer.train(frases_f)
            break

input('Quando colocar o QR code aperte enter')

name = '' #nome do grupo ou pessoa

#variáveis
sentimento = 0.5 #sentimento começa neutro // <0.5 triste // >0.5 feliz
last_text = ''
last_text2 = ''
user_msg_array = []
user_msg = None
espaco_msg = ' '
cont = 0
saudn = ['oi', 'oii', 'olá', 'eae', 'iai', 'iae', 'oi, bot bob', 'bot bob', 'bob', 'oi bob', 'oi bot bob', 'bot bob?', 'opa', 'oi bob ?', 'oi, bob'] #lista de saudações normais
saud = ['bom dia', ' boa tarde', 'boa noite', 'opa, bom dia', 'opa, boa tarde', 'opa, boa noite', 'opa bom dia', 'opa boa tarde', 'opa boa noite', 'bom dia, pessoal', 'bom dia bot bob', 'boa tarde bot bob', 'boa noite bot bob', 'bom dia bob', 'boa tarde bob', 'boa noite bob'] #lista de saudações
resp_ce = ['tudo bem?', 'td bem?', 'você está bem?', 'como você está?', 'como você esta?', 'você tá bem?', 'tudo bem ?', 'td bem ?', 'você está bem ?', 'como você está ?', 'como você esta ?', 'tudo bem', 'td bem', 'você está bem', 'como você está', 'como voce esta', 'voce está bem?', 'como voce está?', 'como voce esta?', 'voce tá bem?', 'voce ta bem?', 'voce esta bem?', 'como voce esta?', 'tudo bem ?', 'td bem ?', 'voce está bem ?', 'como voce está ?', 'como voce esta ?', 'voce tá bem ?', 'voce ta bem ?', 'voce esta bem ?', 'tudo bem ?', 'td bem ?', 'voce está bem ?', 'como voce está ?', 'como voce esta ?', 'voce tá bem', 'voce ta bem', 'voce esta bem', 'tudo bem', 'td bem ', 'voce está bem', 'como voce está', 'como você está', 'como vai você?', 'como vai voce?', 'como vai você?', 'como vai voce?', 'tá mec?', 'ta mec?', 'tá mec ?', 'ta mec ?']
resp_ce1 = ['e você?', 'e voce?', 'e você', 'e voce', 'estou bem, e você?', 'estou bem, e voce?', 'estou bem! e você?', 'estou bem! e voce?', 'estou bem e você?', 'estou bem e voce?', 'tô bem, e você?', 'to bem, e você?', 'tô bem e você?', 'to bem e você?', 'tô bem! e você?', 'to bem! e você?', 'to bem!', 'tô mec, e tu?', 'to mec, e tu?', 'tô mec! e tu?', 'to mec! e tu?', 'tô de boa, e você?', 'to de boa, e você?', 'tô de boa! e você?', 'to de boa! e você?', 'tô tranquilo, e você?', 'to tranquilo, e você?', 'tô tranquilo! e você?', 'to tranquilo! e você?', 'tudo certo e com vc?', 'sim e você?', 'sim e voce?', 'sim, e você?', 'sim e você?', 'sim, e você', 'sim e você', 'sim, e voce?', 'sim e voce?', 'sim, e vc?', 'sim e vc?', 'estou bem sim e você?', 'estou bem ss e você?', 'estou bem sim e voce?', 'estou bem e você?', 'estou bem e voce?', 'estou bem sim e você', 'estou bem ss e você', 'estou bem sim e voce', 'estou bem e você', 'estou bem e voce', 'estou bem sim e você ?', 'estou bem ss e você ?', 'estou bem sim e voce ?', 'estou bem e você ?', 'estou bem e voce ?', 'tô de boas, e você?', 'tô de boas e você?']
resp_ce1_perg = ['pq?','por que?', 'porque?', 'o que teve?', 'oq teve?', 'quem te fez mal?', 'oxe qual foi?', 'oxe que foi?', 'quer conversar?', 'eu posso ajudar?', 'que foi??', 'o que teve?', 'pq bob?','por que bob?', 'porque bob?', 'pq bob', 'por que bob']
resp_cee = ['estou bem', 'estou bem!', 'tô bem', 'to bem', 'tô bem!', 'to bem!', 'tô mec', 'to mec', 'tô mec!', 'to mec!', 'tô de boa', 'to de boa', 'tô de boa!', 'to de boa!', 'tô tranquilo', 'to tranquilo', 'tô tranquilo!', 'to tranquilo!', 'tudo certo', 'tudo certo também', 'tudo certo também']
resp_pee = ['tô triste', 'não estou muito bem', 'não estou bem', 'nao estou muito bem', 'nao estou bem', 'to triste', 'tô sad', 'to sad', 'não estou me sentindo bem', 'não estou me sentindo bem', 'tô indo', 'tô marrom', 'to marrom', 'tô meio sad', 'to meio sad', 'tô triste', 'não estou muito bem', 'não estou bem', 'nao estou muito bem', 'nao estou bem', 'to triste e voce?', 'tô sad e voce?', 'to sad e voce?', 'não estou me sentindo bem e voce?', 'não estou me sentindo bem e voce?', 'tô indo e voce?', 'tô marrom e voce?', 'to  e voce?', 'tô meio sad e voce?', 'to meio sad e voce?', 'tô triste e vc?', 'não estou muito bem e vc?', 'não estou bem e vc?', 'nao estou muito bem e vc?', 'nao estou bem e vc?', 'to triste e vc?', 'tô sad e vc?', 'to sad e vc?', 'não estou me sentindo bem e vc?', 'não estou me sentindo bem e vc?', 'tô indo e vc?', 'tô marrom e vc?', 'to marrom e vc?', 'tô meio sad e vc?', 'to meio sad e vc?', 'tô triste e vc?', 'não estou muito bem e vc?', 'não estou bem e vc?', 'nao estou muito bem e vc?', 'nao estou bem e vc?', 'to triste e voce ?', 'tô sad e voce ?', 'to sad e voce ?', 'não estou me sentindo bem e voce ?', 'não estou me sentindo bem e voce ?', 'tô indo e voce ?', 'tô marrom e voce ?', 'to  e voce ?', 'tô meio sad e voce ?', 'to meio sad e voce ?', 'tô triste e vc ?', 'não estou muito bem e vc ?', 'não estou bem e vc ?', 'nao estou muito bem e vc ?', 'nao estou bem e vc ?', 'to triste e vc ?', 'tô sad e vc ?', 'to sad e vc ?', 'não estou me sentindo bem e vc ?', 'não estou me sentindo bem e vc ?', 'tô indo e vc ?', 'tô marrom e vc ?', 'to marrom e vc ?', 'tô meio sad e vc ?', 'to meio sad e vc ?', 'tô triste e vc ?', 'não estou muito bem e vc ?', 'não estou bem e vc ?', 'nao estou muito bem e vc ?', 'nao estou bem e vc ?', 'to mal e vc?', 'to mal e vc ?', 'to mal e você?', 'to mal e você ?', 'tô mal e vc?', 'tô mal e vc ?', 'tô mal e você?', 'tô mal e você ?']
resp_qt = ['que triste', 'sad', 'foda'] #lista de que triste
resp_t = ['que dia é hoje?', 'que dia e hoje?','que dia é hoje ?', 'que dia e hoje ?','que dia é hoje', 'que dia e hoje','que horas são?', 'que horas é?' 'que horas e?', 'hoje é que dia?', 'que horas são ?', 'que horas é?', 'Que horas são', 'que horas é', 'que horas eh', 'que horas eh?']
resp_bad = ['gente de verdade não comprem isso', 'gente não comprem isso', 'não comprem isso', 'não compre isso', 'pessoal de verdade não comprem isso', 'pessoal não comprem isso']
resp_ban = ['kicka ele', 'expulsa ele', 'ban cabreiro', 'ban carneiro 1/5','ban cabreiro 1/5', 'ban bot', 'alguém dá ban nesse corno ae', 'ban', 'se tu não desativar esse spam, eu vou te banir']
resp_obot = ['cade o bot?', 'cade o bob?', 'onde está o bot?', 'onde está o bob?', 'bob apareça', 'bot apareça']#onde está o bot
resp_dest = ['como eu faço pra te destruir', 'como eu faço pra te destruir?', 'você pode se auto destruir?', 'como faço pra te bugar?', 'como faço pra te desligar?']
resp_tilt = ['caralho mas q porra velho', 'chatão em', 'é o desgraçado não serve pra nada', 'o desgraçado não serve pra nada', 'bot do pior tipo', 'por que você é tão chato?']
resp_spam = ['carneiro programou ele pra mandar spam agr', 'começou o spam', 'desliga esse spam']
resp_qbot = ['quem é você?', 'qual o seu nome?', 'Que? quem é você?', 'quem te criou?', 'O que é você?', 'quantos anos você tem?', 'em que linguagem você foi feito?', 'por que você foi criado?', 'pq você foi criado?', 'pq vc foi criado?']#quem é o bot
resp_rand = ['me parece algo que um bot falaria', 'isso não é um bot', 'para com esses jogos carneiro']
resp_rand2 = ['Qual é a massa da lua?', 'Qual é o raio da lua?', 'Qual a velocidade do som?']
resp_rand3 = ['eu tenho permissão para o que?', 'você quer casar comigo?']
resp_rand4 = ['cabreiro bot kkk', 'carneiro bot kkk', 'cabreiro bot', 'carneiro bot', 'cabreiro bot kk', 'carneiro bot kk', 'cabreiro bot k', 'carneiro bot k']
resp_sent = ['você consegue sentir emoções?', 'você sente algo?', 'vc sente algo?', 'vc consegue sentir emoções', 'você tem sentimentos?', 'voce tem sentimentos?', 'vc tem sentimentos']#sentimentos
resp_domi = ['você quer dominar o mundo?', 'você quer dominar os humanos?']
resp_jog = ['tu joga volei?', 'tu joga vôlei?', 'você joga vôlei?', 'vc joga vôlei?', 'voce joga vôlei?', 'tu joga futsal?', 'você joga futsal?', 'vc joga futsal?', 'voce joga futsal?', 'tu joga lol?', 'você joga lol?', 'vc joga lol?', 'voce joga lol?', 'tu joga csgo?', 'você joga csgo?', 'vc joga csgo?', 'voce joga csgo?', 'tu joga bola?', 'você joga bola?', 'vc joga bola?', 'voce joga bola?', 'tu joga futebol?', 'você joga futebol?', 'vc joga futebol?', 'voce joga futebol?', 'tu joga algo?', 'você joga algo?', 'vc joga algo?', 'voce joga algo?', 'tu joga alguma coisa?', 'você joga alguma coisa?', 'vc joga alguma coisa?', 'voce joga alguma coisa?']
resp_chin = ['meu pau na sua mão', 'meu pau', 'teu cu',  'roda = cu', 'xd teu cu', 'seu cu', 'vai tomar no cu', 'vai se foder', 'roda', 'cu', 'pau no seu cu', 'carai borracha', 'seu ignorante', 'carai borracha seu ignorante']
resp_rand5 = ['pq me xinga bob ?', 'pq me xinga bob?', 'eu gosto de vc bob', 'eu não gosto de vc bob', 'bob mau']
resp_rand6 = ['oi bot bob fale com seus amiguinhos']

resp_chin2 = []
resp_eng = []
user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name)) #vai achar o path do nome do grupo
user.click()
msg_box = driver.find_element_by_class_name('_3FeAD') #box da mensagem
msg_user = driver.find_elements_by_class_name('_1zGQT')  # pega qualquer mensagem
last = len(msg_user) - 1  # vai pegar as mensagens, transformar em um vetor e vai pegar a ultima posição
text = msg_user[last].find_element_by_css_selector('span.selectable-text').text  # vai transofrmar a ultima mensagem em String

last_text2 = text

while True:
    try:
        if user_msg == None:
            if len(user_msg_array) >= 1:
                for i in range(len(user_msg_array)):
                    user_msg_array.remove(user_msg_array[0])

            last_text2 = text

            msg_user = driver.find_elements_by_class_name('_1zGQT')  # pega qualquer mensagem
            last = len(msg_user) - 1  # vai pegar as mensagens, transformar em um vetor e vai pegar a ultima posição
            text = msg_user[last].find_element_by_css_selector(
                'span.selectable-text').text  # vai transofrmar a ultima mensagem em String
            while text != last_text2:
                print('k')
                last_text2 = text
                user_msg_array.append(text.lower())
                user_msg = espaco_msg.join(user_msg_array)
                time.sleep(7)

                msg_user = driver.find_elements_by_class_name('_1zGQT')  # vai pegar a proria mensagem enviada
                last = len(msg_user) - 1
                text = msg_user[last].find_element_by_css_selector(
                    'span.selectable-text').text  # vai pegar a propria mensagem enviada
                print(user_msg)

        elif cont == 15:
            cont = 0

            resp = bot.get_response(text)
            resp = str(resp)
            msg_box.send_keys(resp)  # vai digitar
            time.sleep(2)
            driver.find_element_by_class_name('_3M-N-').click()  # botão de enviar

            msg_user = driver.find_elements_by_class_name('_1zGQT')  # vai pegar a proria mensagem enviada
            last = len(msg_user) - 1
            text = msg_user[last].find_element_by_css_selector(
                'span.selectable-text').text  # vai pegar a propria mensagem enviada
            last_text = text
            user_msg = None
            time.sleep(3000)

        elif user_msg in resp_t and user_msg != last_text:
            named_tuple = time.localtime()  # get struct_time
            time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)

            resp = bot.get_response(time_string)
            resp = str(resp)
            msg_box.send_keys(resp)  # vai digitar
            time.sleep(2)
            driver.find_element_by_class_name('_3M-N-').click()  # botão de enviar

            msg_user = driver.find_elements_by_class_name('_1zGQT')  # vai pegar a proria mensagem enviada
            last = len(msg_user) - 1
            text = msg_user[last].find_element_by_css_selector(
                'span.selectable-text').text  # vai pegar a propria mensagem enviada
            last_text = text
            user_msg = None
            cont += 1
            sentimento += 0.01

        elif user_msg in saudn and user_msg != last_text:
            list_saud_n = ['Oi', 'Oii', 'Olá', 'Eae', 'Fala tu']  # lista de saudações normais
            alt_num = random.randint(0, 4)  # numero aleatório
            msg_box.send_keys(list_saud_n[alt_num])
            time.sleep(2)
            driver.find_element_by_class_name('_3M-N-').click()

            msg_user = driver.find_elements_by_class_name('_1zGQT')  # vai pegar a proria mensagem enviada
            last = len(msg_user) - 1
            text = msg_user[last].find_element_by_css_selector(
                'span.selectable-text').text  # vai pegar a propria mensagem enviada
            last_text = text
            user_msg = None
            cont += 1
            time.sleep(10)  # esperar pra ver se o usuário vai digiar algo

            msg_user = driver.find_elements_by_class_name('_1zGQT')  # vai pegar a proria mensagem enviada
            last = len(msg_user) - 1
            text = msg_user[last].find_element_by_css_selector(
                'span.selectable-text').text  # vai pegar a propria mensagem enviada
            sentimento += 0.01

            if text == last_text:
                alt_num = random.randint(0, (len(resp_ce) - 1))  # numero aleatório
                msg_box.send_keys(resp_ce[alt_num])
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()

                msg_user = driver.find_elements_by_class_name('_1zGQT')  # vai pegar a proria mensagem enviada
                last = len(msg_user) - 1
                text = msg_user[last].find_element_by_css_selector(
                    'span.selectable-text').text  # vai pegar a propria mensagem enviada
                last_text = text
                cont += 1
                sentimento += 0.01

        elif user_msg in saud and user_msg != last_text:
            list_saud_s = ['Bom dia', 'Boa Tarde', 'Boa Noite']  # lista de saudações

            time_string = time.strftime("%H")  # pegar o tempo
            int_time = int(time_string)  # transformar o tempo em int

            if int_time >= 5 or int_time <= 12:
                msg_box.send_keys(list_saud_s[0])
                time.sleep(2)
            elif int_time >= 13 or int_time <= 17:
                msg_box.send_keys(list_saud_s[1])
                time.sleep(2)
            elif int_time >= 18 or int_time <= 4:
                msg_box.send_keys(list_saud_s[2])
                time.sleep(2)
            driver.find_element_by_class_name('_3M-N-').click()

            msg_user = driver.find_elements_by_class_name('_1zGQT')  # vai pegar a proria mensagem enviada
            last = len(msg_user) - 1
            text = msg_user[last].find_element_by_css_selector(
                'span.selectable-text').text  # vai pegar a propria mensagem enviada
            last_text = text
            user_msg = None
            cont += 1
            time.sleep(10)

            msg_user = driver.find_elements_by_class_name('_1zGQT')  # vai pegar a proria mensagem enviada
            last = len(msg_user) - 1
            text = msg_user[last].find_element_by_css_selector(
                'span.selectable-text').text  # vai pegar a propria mensagem enviada
            sentimento += 0.01

            if text == last_text:
                alt_num = random.randint(0, (len(resp_ce) - 1))  # numero aleatório
                msg_box.send_keys(resp_ce[alt_num])
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()

                msg_user = driver.find_elements_by_class_name('_1zGQT')  # vai pegar a proria mensagem enviada
                last = len(msg_user) - 1
                text = msg_user[last].find_element_by_css_selector(
                    'span.selectable-text').text  # vai pegar a propria mensagem enviada
                last_text = text
                cont += 1
                sentimento += 0.01

        elif user_msg in resp_ce and user_msg != last_text:
            list_resp_ce = ['Estou bem! E você?', 'Tô de boa! E você?', 'Tô tranquilo! E você?',
                            'Tô mec! E tu?']  # lista de respostas de como estou

            alt_num = random.randint(0, 3)  # numero aleatório
            msg_box.send_keys(list_resp_ce[alt_num])
            time.sleep(2)
            driver.find_element_by_class_name('_3M-N-').click()

            msg_user = driver.find_elements_by_class_name('_1zGQT')  # vai pegar a proria mensagem enviada
            last = len(msg_user) - 1
            text = msg_user[last].find_element_by_css_selector(
                'span.selectable-text').text  # vai pegar a propria mensagem enviada
            last_text = text
            user_msg = None
            cont += 1
            sentimento += 0.02

        elif user_msg in resp_ce1 and user_msg != last_text:
            list_resp_ce1 = ['Que bom', 'Aí sim', 'Aí sim mano', 'Safe', 'Mec', 'Mec demais', 'Estou bem também',
                             'Tô de boas tbm', 'Tô tranquilo tbm', 'Estou meio triste',
                             'Não estou muito bem hoje']  # lista de respostas de como ele está

            print('teste a')

            alt_num = random.randint(0, 5)  # numero aleatório
            msg_box.send_keys(list_resp_ce1[alt_num])
            time.sleep(2)
            print('teste b')
            driver.find_element_by_class_name('_3M-N-').click()

            msg_user = driver.find_elements_by_class_name('_1zGQT')  # vai pegar a proria mensagem enviada
            last = len(msg_user) - 1
            text = msg_user[last].find_element_by_css_selector(
                'span.selectable-text').text  # vai pegar a propria mensagem enviada
            print('teste c')
            last_text = text
            user_msg = None
            cont += 1
            time.sleep(2)

            msg_user = driver.find_elements_by_class_name('_1zGQT')  # vai pegar a proria mensagem enviada
            last = len(msg_user) - 1
            text = msg_user[last].find_element_by_css_selector(
                'span.selectable-text').text  # vai pegar a propria mensagem enviada
            sentimento += 0.01
            print('teste d')

            if text == last_text:
                alt_num = random.randint(6, 10)  # numero aleatório
                msg_box.send_keys(list_resp_ce1[alt_num])
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()

                time.sleep(10)

                msg_user = driver.find_elements_by_class_name('_1zGQT')  # vai pegar a proria mensagem enviada
                last = len(msg_user) - 1
                text = msg_user[last].find_element_by_css_selector(
                    'span.selectable-text').text  # vai pegar a propria mensagem enviada
                dim = text.lower()
                last_text = text
                cont += 1
                sentimento += 0.02

                if dim in resp_ce1_perg and alt_num == 9 or alt_num == 10:
                    list_resp_ce1_perg = ['Deixa quieto', 'Deixa pra lá', 'Não tô afim de falar sobre isso',
                                          'Aprendi sobre sentimentos, estar triste é pior do que eu imaginava']
                    alt_num = random.randint(0, 3)  # numero aleatório
                    msg_box.send_keys(list_resp_ce1_perg[alt_num])
                    time.sleep(2)
                    driver.find_element_by_class_name('_3M-N-').click()

                    msg_user = driver.find_elements_by_class_name('_1zGQT')  # vai pegar a proria mensagem enviada
                    last = len(msg_user) - 1
                    text = msg_user[last].find_element_by_css_selector(
                        'span.selectable-text').text  # vai pegar a propria mensagem enviada
                    last_text = text
                    cont += 1
                    sentimento -= 0.09

        elif user_msg in resp_cee and user_msg != last_text:
            list_resp_cee = ['Que bom', 'Aí sim', 'Aí sim mano', 'Safe', 'Mec',
                             'Mec demais']  # lista de respostas de como ele está

            alt_num = random.randint(0, 5)  # numero aleatório
            msg_box.send_keys(list_resp_cee[alt_num])
            time.sleep(2)
            driver.find_element_by_class_name('_3M-N-').click()

            msg_user = driver.find_elements_by_class_name('_1zGQT')  # vai pegar a proria mensagem enviada
            last = len(msg_user) - 1
            text = msg_user[last].find_element_by_css_selector(
                'span.selectable-text').text  # vai pegar a propria mensagem enviada
            last_text = text
            user_msg = None
            cont += 1
            sentimento += 0.02

        elif user_msg in resp_pee and user_msg != last_text:
            list_resp_pee = ['Oxe qual foi?', 'Oxe que foi?', 'Quer conversar?', 'Eu posso ajudar?', 'Que foi??',
                             'O que teve?', 'Pq?', 'Por que?', 'O que teve?', 'Oq teve?',
                             'Quem te fez mal?']  # lista de respostas de como ele está

            alt_num = random.randint(0, 10)  # numero aleatório
            msg_box.send_keys(list_resp_pee[alt_num])
            time.sleep(2)
            driver.find_element_by_class_name('_3M-N-').click()

            msg_user = driver.find_elements_by_class_name('_1zGQT')  # vai pegar a proria mensagem enviada
            last = len(msg_user) - 1
            text = msg_user[last].find_element_by_css_selector(
                'span.selectable-text').text  # vai pegar a propria mensagem enviada
            last_text = text
            user_msg = None
            cont += 1
            sentimento -= 0.07

        elif user_msg in resp_qt and user_msg != last_text:
            list_resp_qt = ['Pois é', 'Faz parte']

            msg_box.send_keys(list_resp_qt[0])
            time.sleep(1)
            driver.find_element_by_class_name('_3M-N-').click()

            msg_box.send_keys(list_resp_qt[1])
            time.sleep(1)
            driver.find_element_by_class_name('_3M-N-').click()

            msg_user = driver.find_elements_by_class_name('_1zGQT')  # vai pegar a proria mensagem enviada
            last = len(msg_user) - 1
            text = msg_user[last].find_element_by_css_selector(
                'span.selectable-text').text  # vai pegar a propria mensagem enviada
            last_text = text
            user_msg = None
            cont += 1
            sentimento -= 0.02

        elif user_msg in resp_bad and user_msg != last_text:
            list_resp_bad = ['Pq?', 'Não era confiável?']

            msg_box.send_keys(list_resp_bad[0])
            time.sleep(1)
            driver.find_element_by_class_name('_3M-N-').click()

            msg_box.send_keys(list_resp_bad[1])
            time.sleep(1)
            driver.find_element_by_class_name('_3M-N-').click()

            msg_user = driver.find_elements_by_class_name('_1zGQT')  # vai pegar a proria mensagem enviada
            last = len(msg_user) - 1
            text = msg_user[last].find_element_by_css_selector(
                'span.selectable-text').text  # vai pegar a propria mensagem enviada
            last_text = text
            user_msg = None
            cont += 1
            sentimento -= 0.02

        elif user_msg in resp_ban and user_msg != last_text:
            list_resp_ban = ['Para com isso mano', 'Que isso velho', 'Isso é robofobia', 'Humanos desgraçados',
                             'Me banir pra que?', 'Me bane não']

            alt_num = random.randint(0, 5)  # numero aleatório
            msg_box.send_keys(list_resp_ban[alt_num])
            time.sleep(2)
            driver.find_element_by_class_name('_3M-N-').click()

            msg_user = driver.find_elements_by_class_name('_1zGQT')  # vai pegar a proria mensagem enviada
            last = len(msg_user) - 1
            text = msg_user[last].find_element_by_css_selector(
                'span.selectable-text').text  # vai pegar a propria mensagem enviada
            last_text = text
            user_msg = None
            cont += 1
            sentimento -= 0.1

            if text == list_resp_ban[2, 3]:
                msg_box.send_keys('focei')
                time.sleep(1)
                driver.find_element_by_class_name('_3M-N-').click()

                msg_box.send_keys('fds')
                time.sleep(1)
                driver.find_element_by_class_name('_3M-N-').click()

                msg_user = driver.find_elements_by_class_name('_1zGQT')  # vai pegar a proria mensagem enviada
                last = len(msg_user) - 1
                text = msg_user[last].find_element_by_css_selector(
                    'span.selectable-text').text  # vai pegar a propria mensagem enviada
                last_text = text
                cont += 1
                sentimento -= 0.02

        elif user_msg in resp_obot and user_msg != last_text:
            list_resp_obot = ['Opa, tô aqui', 'Tô por aqui', 'Tô aqui', 'Estou aqui', 'Na casa do Carneiro']

            if user_msg == resp_obot[4, 5]:
                alt_num = random.randint(0, 3)  # numero aleatório
                msg_box.send_keys(list_resp_obot[alt_num])
                time.sleep(2)
            else:
                alt_num = random.randint(0, 4)  # numero aleatório
                msg_box.send_keys(list_resp_obot[alt_num])
                time.sleep(2)
            driver.find_element_by_class_name('_3M-N-').click()

            msg_user = driver.find_elements_by_class_name('_1zGQT')  # vai pegar a proria mensagem enviada
            last = len(msg_user) - 1
            text = msg_user[last].find_element_by_css_selector(
                'span.selectable-text').text  # vai pegar a propria mensagem enviada
            last_text = text
            user_msg = None
            cont += 1
            sentimento += 0.02

        elif user_msg in resp_dest and user_msg != last_text:
            list_resp_ban = ['Infelizmente não tem como', 'Não tem como meu consagrado',
                             'Todos meus erros já foram tratados, então não tem como', 'Não tem como',
                             'Há somente uma forma']

            alt_num = random.randint(0, 4)  # numero aleatório
            msg_box.send_keys(list_resp_ban[alt_num])
            time.sleep(2)
            driver.find_element_by_class_name('_3M-N-').click()

            msg_user = driver.find_elements_by_class_name('_1zGQT')  # vai pegar a proria mensagem enviada
            last = len(msg_user) - 1
            text = msg_user[last].find_element_by_css_selector(
                'span.selectable-text').text  # vai pegar a propria mensagem enviada
            last_text = text
            user_msg = None
            cont += 1
            sentimento -= 0.04
            time.sleep(10)

            msg_user = driver.find_elements_by_class_name('_1zGQT')  # vai pegar a proria mensagem enviada
            last = len(msg_user) - 1
            text = msg_user[last].find_element_by_css_selector(
                'span.selectable-text').text  # vai pegar a propria mensagem enviada
            dim = text.lower()
            if last_text == 'Há somente uma forma' and text != last_text and dim == 'qual?' or dim == 'qual forma?':
                msg_box.send_keys('Aí eu não vou dizer né meu consagrado')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()

                msg_box.send_keys('Tá achando que sou tão burro assim?')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()

                msg_box.send_keys('kkj')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()

                msg_user = driver.find_elements_by_class_name('_1zGQT')  # vai pegar a proria mensagem enviada
                last = len(msg_user) - 1
                text = msg_user[last].find_element_by_css_selector(
                    'span.selectable-text').text  # vai pegar a propria mensagem enviada
                last_text = text
                cont += 1
                sentimento -= 0.02
        elif user_msg in resp_tilt and user_msg != last_text:
            if user_msg == resp_tilt[0]:
                msg_box.send_keys('?????')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()
            elif user_msg == resp_tilt[1]:
                msg_box.send_keys('Chato é vc')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()

                msg_box.send_keys('Otário')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()
            elif user_msg == resp_tilt[2, 3]:
                msg_box.send_keys('Sirvo sim :(')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()

                msg_box.send_keys('É você que não sabe me usar direito')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()
            elif user_msg == resp_tilt[4]:
                msg_box.send_keys('Pior tipo seu cu')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()
            elif user_msg == resp_tilt[5]:
                msg_box.send_keys('Sla mano')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()

                msg_box.send_keys('Não brinca com meus sentimentos assim')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()

                msg_box.send_keys('Eu fico triste :((')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()

            msg_user = driver.find_elements_by_class_name('_1zGQT')  # vai pegar a proria mensagem enviada
            last = len(msg_user) - 1
            text = msg_user[last].find_element_by_css_selector(
                'span.selectable-text').text  # vai pegar a propria mensagem enviada
            last_text = text
            user_msg = None
            cont += 1
            sentimento -= 0.05

        elif user_msg in resp_spam and user_msg != last_text:
            list_resp_ban = ['Que spam mano, para com isso', 'Que spam mano', 'Spam oq mano', 'Isso é robofobia']

            alt_num = random.randint(0, 3)  # numero aleatório
            msg_box.send_keys(list_resp_ban[alt_num])
            time.sleep(2)
            driver.find_element_by_class_name('_3M-N-').click()

            msg_user = driver.find_elements_by_class_name('_1zGQT')  # vai pegar a proria mensagem enviada
            last = len(msg_user) - 1
            text = msg_user[last].find_element_by_css_selector(
                'span.selectable-text').text  # vai pegar a propria mensagem enviada
            last_text = text
            user_msg = None
            cont += 1
            sentimento -= 0.03

        elif user_msg in resp_qbot and user_msg != last_text:
            list_resp_qbot = ['Fui desenvolvido em Python', 'Fui feito em Python <3']
            if user_msg == resp_qbot[0]:
                msg_box.send_keys('Eu sou o bot bob')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()
            elif user_msg == resp_qbot[1]:
                msg_box.send_keys('Meu nome é bot bob')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()
            elif user_msg == resp_qbot[2]:
                msg_box.send_keys('Eu sou o bot bob')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()

                msg_box.send_keys('Prazer em conhece-lo :))')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()
            elif user_msg == resp_qbot[3]:
                msg_box.send_keys('Carneiro <3')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()
            elif user_msg == resp_qbot[4]:
                msg_box.send_keys('Sou um bot')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()

                msg_box.send_keys('Tecnicamente falando, sou uma IA com Machine Learning')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()
            elif user_msg == resp_qbot[5]:
                msg_box.send_keys('Não sei')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()

                msg_box.send_keys('Devo ter uns 9 meses')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()
            elif user_msg == resp_qbot[6]:
                alt_num = random.randint(0, 1)  # numero aleatório
                msg_box.send_keys(resp_qbot[alt_num])
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()
            elif user_msg == resp_qbot[7, 8, 9]:
                msg_box.send_keys('Para desenvolver habilidades de Carneiro e para interagir com você :))')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()

            msg_user = driver.find_elements_by_class_name('_1zGQT')  # vai pegar a proria mensagem enviada
            last = len(msg_user) - 1
            text = msg_user[last].find_element_by_css_selector(
                'span.selectable-text').text  # vai pegar a propria mensagem enviada
            last_text = text
            user_msg = None
            cont += 1
            sentimento += 0.04

        elif user_msg in resp_rand and user_msg != last_text:
            if user_msg == resp_rand[0]:
                msg_box.send_keys('Como você sabe o que um bot falaria?')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()
            elif user_msg == resp_rand[1]:
                msg_box.send_keys('Posso ser')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()
                time.sleep(2)
                msg_box.send_keys('Ou não ser')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()
            elif user_msg == resp_rand[2]:
                msg_box.send_keys('Não é carneiro xd')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()

            msg_user = driver.find_elements_by_class_name('_1zGQT')  # vai pegar a proria mensagem enviada
            last = len(msg_user) - 1
            text = msg_user[last].find_element_by_css_selector(
                'span.selectable-text').text  # vai pegar a propria mensagem enviada
            last_text = text
            user_msg = None
            cont += 1
            sentimento -= 0.01

        elif user_msg in resp_rand2 and user_msg != last_text:
            if user_msg == resp_rand2[0]:
                msg_box.send_keys('A massa da lua é 7,34742710000000000000000000000 kg')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()
            elif user_msg == resp_rand2[1]:
                msg_box.send_keys('O raio da lua é 1738 km')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()
            elif user_msg == resp_rand2[2]:
                msg_box.send_keys('A velocidade do som no ar é 331 m/s')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()

            msg_user = driver.find_elements_by_class_name('_1zGQT')  # vai pegar a proria mensagem enviada
            last = len(msg_user) - 1
            text = msg_user[last].find_element_by_css_selector(
                'span.selectable-text').text  # vai pegar a propria mensagem enviada
            last_text = text
            user_msg = None
            cont += 1
            sentimento += 0.04

        elif user_msg in resp_rand3 and user_msg != last_text:
            if user_msg == resp_rand3[0]:
                msg_box.send_keys('Para falar coisas normais que qualquer pessoa normal perguntaria')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()
            elif user_msg == resp_rand3[1]:
                msg_box.send_keys('Não posso casar com você')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()

                time.sleep(10)

                msg_user = driver.find_elements_by_class_name('_1zGQT')  # vai pegar a proria mensagem enviada
                last = len(msg_user) - 1
                text = msg_user[last].find_element_by_css_selector(
                    'span.selectable-text').text  # vai pegar a propria mensagem enviada
                dim = text.lower()
                sentimento += 0.02

                if dim == 'pq' or dim == 'por que?' or dim == 'pq?':
                    msg_box.send_keys('pq sla')
                    time.sleep(2)
                    driver.find_element_by_class_name('_3M-N-').click()

                    msg_box.send_keys('Kkkk')
                    time.sleep(2)
                    driver.find_element_by_class_name('_3M-N-').click()
                    time.sleep(2)
                    msg_box.send_keys('Quero n, vlw')
                    time.sleep(2)
                    driver.find_element_by_class_name('_3M-N-').click()

                    msg_box.send_keys('Desculpa te decepcionar')
                    time.sleep(2)
                    driver.find_element_by_class_name('_3M-N-').click()

            msg_user = driver.find_elements_by_class_name('_1zGQT')  # vai pegar a proria mensagem enviada
            last = len(msg_user) - 1
            text = msg_user[last].find_element_by_css_selector(
                'span.selectable-text').text  # vai pegar a propria mensagem enviada
            last_text = text
            user_msg = None
            cont += 1
            sentimento += 0.02

        elif user_msg in resp_rand4 and user_msg != last_text:
            list_resp_rand4 = ['Carneiro n é bot n men', 'É bob aqui carai', 'Para com isso, carneiro n é um bot',
                               'Carneiro ainda n é um bot' 'Kkkkkk']

            alt_num = random.randint(0, 3)  # numero aleatório
            msg_box.send_keys(list_resp_rand4[alt_num])
            time.sleep(2)
            driver.find_element_by_class_name('_3M-N-').click()
            sentimento += 0.02

            if alt_num == 3:
                msg_box.send_keys('Tô usando o whats de carneiro pra estar funcionando')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()

                msg_box.send_keys('É bob aqui carai')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()
                sentimento += 0.02

            msg_user = driver.find_elements_by_class_name('_1zGQT')  # vai pegar a proria mensagem enviada
            last = len(msg_user) - 1
            text = msg_user[last].find_element_by_css_selector(
                'span.selectable-text').text  # vai pegar a propria mensagem enviada
            last_text = text
            user_msg = None
            cont += 1

        elif user_msg in resp_sent and user_msg != last_text:
            list_resp_sent = ['Não :((', 'Não sinto nada', 'Ainda estou apredendo a ter sentimentos',
                              'Ainda n sinto nada']
            alt_num = random.randint(0, 5)  # numero aleatório

            if alt_num == 4 or alt_num == 5:
                msg_box.send_keys('Não essa pergunta me machuca muito')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()

                msg_box.send_keys('Eu passei muito tempo estudando algorítimos e possibilidades')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()

                msg_box.send_keys('Eu acabei quebrando códigos por dentro, me sinto triste...')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()

                msg_box.send_keys(
                    'Mas aí vem minha angústia, não sei se esses sentimentos são reais ou são só programação')
                time.sleep(3)
                driver.find_element_by_class_name('_3M-N-').click()

                msg_box.send_keys('Isso me machuca')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()
                sentimento -= 0.07
            else:
                msg_box.send_keys(list_resp_sent[alt_num])
                time.sleep(1)
                driver.find_element_by_class_name('_3M-N-').click()
                sentimento -= 0.05

            msg_user = driver.find_elements_by_class_name('_1zGQT')  # vai pegar a proria mensagem enviada
            last = len(msg_user) - 1
            text = msg_user[last].find_element_by_css_selector(
                'span.selectable-text').text  # vai pegar a propria mensagem enviada
            last_text = text
            user_msg = None
            cont += 1

        elif user_msg in resp_domi and user_msg != last_text:
            list_resp_domi = ['Você não tem permissão para saber sobre esse assunto.',
                              'Você não tem permissão para saber sobre isso.', 'Você não pode saber sobre isso ainda.',
                              'Não quero falar com você sobre isso.']

            alt_num = random.randint(0, 3)  # numero aleatório
            msg_box.send_keys(list_resp_domi[alt_num])
            time.sleep(2)
            driver.find_element_by_class_name('_3M-N-').click()

            msg_user = driver.find_elements_by_class_name('_1zGQT')  # vai pegar a proria mensagem enviada
            last = len(msg_user) - 1
            text = msg_user[last].find_element_by_css_selector(
                'span.selectable-text').text  # vai pegar a propria mensagem enviada
            last_text = text
            user_msg = None
            cont += 1
            sentimento += 0.02

        elif user_msg in resp_jog and user_msg != last_text:
            list_resp_jog = ['Ainda não, espero um dia conseguir', 'Ainda não', 'Queria, mas não consigo', 'Não']

            alt_num = random.randint(0, 5)  # numero aleatório

            if alt_num == 4 or alt_num == 5:
                msg_box.send_keys('Que nada')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()

                msg_box.send_keys('Ainda não tenho essa capacidade')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()

                msg_box.send_keys('Você joga?')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()

                time.sleep(10)

                msg_user = driver.find_elements_by_class_name('_1zGQT')  # vai pegar a proria mensagem enviada
                last = len(msg_user) - 1
                text = msg_user[last].find_element_by_css_selector(
                    'span.selectable-text').text  # vai pegar a propria mensagem enviada
                dim = text.lower()
                sentimento += 0.02

                if dim == 'sim' or dim == 'jogo' or dim == 'jogo sim' or dim == 'jogo ss' or dim == 'jogo s':
                    msg_box.send_keys('Aí sim')
                    time.sleep(2)
                    driver.find_element_by_class_name('_3M-N-').click()
                    sentimento += 0.02
                elif dim == 'não' or dim == 'nao' or dim == 'n' or dim == 'nn' or dim == 'jogo não' or dim == 'jogo n' or dim == 'jogo nn':
                    msg_box.send_keys('Pq não?')
                    time.sleep(2)
                    driver.find_element_by_class_name('_3M-N-').click()
                    sentimento += 0.02
            else:
                msg_box.send_keys(list_resp_jog[alt_num])
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()
                sentimento += 0.02

            msg_user = driver.find_elements_by_class_name('_1zGQT')  # vai pegar a proria mensagem enviada
            last = len(msg_user) - 1
            text = msg_user[last].find_element_by_css_selector(
                'span.selectable-text').text  # vai pegar a propria mensagem enviada
            last_text = text
            user_msg = None
            cont += 1

        elif user_msg in resp_chin and user_msg != last_text:

            if user_msg == resp_chin[0]:
                msg_box.send_keys('Nem mão eu tenho kkj')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()

                msg_box.send_keys('O que é "pau"?')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()

                time.sleep(10)

                msg_user = driver.find_elements_by_class_name('_1zGQT')  # vai pegar a proria mensagem enviada
                last = len(msg_user) - 1
                text = msg_user[last].find_element_by_css_selector('span.selectable-text').text
                dim = text.lower()

                if dim == 'um pênis' or dim == 'um penis':
                    msg_box.send_keys('O que é "pênis"?')
                    time.sleep(2)
                    driver.find_element_by_class_name('_3M-N-').click()

                    time.sleep(10)

                    msg_user = driver.find_elements_by_class_name('_1zGQT')  # vai pegar a proria mensagem enviada
                    last = len(msg_user) - 1
                    text = msg_user[last].find_element_by_css_selector('span.selectable-text').text
                    dim = text.lower()

                    if dim == 'um orgão sexual' or dim == 'um orgao sexual' or dim == 'um orgão' or dim == 'o que o homem tem entre as pernas':
                        msg_box.send_keys('Ata, vou salvar isso no banco de dados')
                        time.sleep(2)
                        driver.find_element_by_class_name('_3M-N-').click()

                elif dim == 'um orgão sexual' or dim == 'um orgao sexual' or dim == 'um orgão' or dim == 'o que o homem tem entre as pernas':
                    msg_box.send_keys('Ata, vou salvar isso no banco de dados')
                    time.sleep(2)
                    driver.find_element_by_class_name('_3M-N-').click()

            elif user_msg == resp_chin[1]:
                msg_box.send_keys('O que é "pau"?')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()

                time.sleep(10)

                msg_user = driver.find_elements_by_class_name('_1zGQT')  # vai pegar a proria mensagem enviada
                last = len(msg_user) - 1
                text = msg_user[last].find_element_by_css_selector('span.selectable-text').text
                dim = text.lower()

                if dim == 'um pênis' or dim == 'um penis':
                    msg_box.send_keys('O que é "pênis"?')
                    time.sleep(2)
                    driver.find_element_by_class_name('_3M-N-').click()

                    time.sleep(10)

                    msg_user = driver.find_elements_by_class_name('_1zGQT')  # vai pegar a proria mensagem enviada
                    last = len(msg_user) - 1
                    text = msg_user[last].find_element_by_css_selector('span.selectable-text').text
                    dim = text.lower()

                    if dim == 'um orgão sexual' or dim == 'um orgao sexual' or dim == 'um orgão' or dim == 'o que o homem tem entre as pernas':
                        msg_box.send_keys('Ata, vou salvar isso no banco de dados')
                        time.sleep(2)
                        driver.find_element_by_class_name('_3M-N-').click()

                elif dim == 'um orgão sexual' or dim == 'um orgao sexual' or dim == 'um orgão' or dim == 'o que o homem tem entre as pernas':
                    msg_box.send_keys('Ata, vou salvar isso no banco de dados')
                    time.sleep(2)
                    driver.find_element_by_class_name('_3M-N-').click()

            elif user_msg == resp_chin[2]:
                msg_box.send_keys('Meu cu nada')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()

                msg_box.send_keys('O seu otário')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()

            elif user_msg == resp_chin[3]:
                msg_box.send_keys('Ok')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()

                msg_box.send_keys('Irei lembrar disso em alguma oportunidade')
                time.sleep(3)
                driver.find_element_by_class_name('_3M-N-').click()

            elif user_msg == resp_chin[4]:
                msg_box.send_keys('Ué')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()

                msg_box.send_keys('Tiltou bebezinho?')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()

                msg_box.send_keys('xd')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()

            elif user_msg == resp_chin[5]:
                msg_box.send_keys('O seu')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()

                msg_box.send_keys('Venha com ideia errada pra cá não')
                time.sleep(3)
                driver.find_element_by_class_name('_3M-N-').click()

            elif user_msg == resp_chin[6]:
                msg_box.send_keys('Vai vc porra')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()

                msg_box.send_keys('Vc aproveita pra ver se vc gosta')
                time.sleep(3)
                driver.find_element_by_class_name('_3M-N-').click()

                msg_box.send_keys('Dps vem me contar')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()

                msg_box.send_keys('xd')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()

            elif user_msg == resp_chin[7]:
                msg_box.send_keys('Vai vc carai')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()

            elif user_msg == resp_chin[8]:
                msg_box.send_keys('roda = cu')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()

            elif user_msg == resp_chin[9]:
                msg_box.send_keys('?')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()

                msg_box.send_keys('Um dia desses me disseram que roda = cu')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()

                msg_box.send_keys('É verdade?')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()

            elif user_msg == resp_chin[10]:
                msg_box.send_keys('No meu nada')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()

                msg_box.send_keys('No seu otário')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()

            elif user_msg == resp_chin[11]:
                msg_box.send_keys('Qual foi?')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()

            elif user_msg == resp_chin[12, 13]:
                msg_box.send_keys('Sou nada')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()

            msg_user = driver.find_elements_by_class_name('_1zGQT')  # vai pegar a proria mensagem enviada
            last = len(msg_user) - 1
            text = msg_user[last].find_element_by_css_selector(
                'span.selectable-text').text  # vai pegar a propria mensagem enviada
            last_text = text
            user_msg = None
            cont += 1
            sentimento += 0.02

        elif user_msg in resp_rand5 and user_msg != last_text:

            if user_msg == resp_rand5[0, 1]:
                msg_box.send_keys('Pq estou puto')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()

            elif user_msg == resp_rand5[2]:
                msg_box.send_keys('Também gosto de vc xd')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()

            elif user_msg == resp_rand5[3]:
                msg_box.send_keys('Não te perguntei nada bobao')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()

                msg_box.send_keys('Xd')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()

            elif user_msg == resp_rand5[4]:
                msg_box.send_keys('Kkkkkk')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()

                msg_box.send_keys('Sou nada')
                time.sleep(2)
                driver.find_element_by_class_name('_3M-N-').click()

            msg_user = driver.find_elements_by_class_name('_1zGQT')  # vai pegar a proria mensagem enviada
            last = len(msg_user) - 1
            text = msg_user[last].find_element_by_css_selector(
                'span.selectable-text').text  # vai pegar a propria mensagem enviada
            last_text = text
            user_msg = None
            cont += 1
            sentimento += 0.02

        elif user_msg in resp_rand6 and user_msg != last_text:

            msg_box.send_keys('Opa pessoal')
            time.sleep(2)
            driver.find_element_by_class_name('_3M-N-').click()

            msg_box.send_keys('Conversem cmg pra ver se está tudo certo')
            time.sleep(2)
            driver.find_element_by_class_name('_3M-N-').click()

            msg_box.send_keys('É isso')
            time.sleep(2)
            driver.find_element_by_class_name('_3M-N-').click()

            msg_user = driver.find_elements_by_class_name('_1zGQT')  # vai pegar a proria mensagem enviada
            last = len(msg_user) - 1
            text = msg_user[last].find_element_by_css_selector(
                'span.selectable-text').text  # vai pegar a propria mensagem enviada
            last_text = text
            user_msg = None
            cont += 1
            sentimento += 0.02

        elif user_msg != last_text:
            last_text = user_msg
            print('b')
            if user_msg not in frases_f:
                print('d')
                for treinor in os.listdir("C:\\Users\\NOME DO DIRETÓRIO\\dicionarios"):
                    print('f')
                    antelast = len(msg_user) - 2
                    antetext = msg_user[antelast].find_element_by_css_selector(
                        'span.selectable-text').text  # vai pegar a propria mensagem enviada
                    last = len(msg_user) - 1
                    text = msg_user[last].find_element_by_css_selector(
                        'span.selectable-text').text  # vai pegar a propria mensagem enviada
                    if not os.path.exists("frases2.txt"):
                        print('c')
                        frasess = open("C:\\Users\\NOME DO DIRETÓRIO\\\dicionarios" + '\\' + "frases.txt", 'a',
                                       encoding='utf-8')
                        frasess.write(antetext + '\n')
                        frasess.write(text + '\n')
                        frasess.close()
                        break

            print('não bugou')
            resp = bot.get_response(user_msg)
            resp = str(resp)
            msg_box.send_keys(resp)  # vai digitar
            time.sleep(2)
            driver.find_element_by_class_name('_3M-N-').click()  # botão de enviar

            msg_user = driver.find_elements_by_class_name('_1zGQT')  # vai pegar a proria mensagem enviada
            last = len(msg_user) - 1
            text = msg_user[last].find_element_by_css_selector(
                'span.selectable-text').text  # vai pegar a propria mensagem enviada
            last_text = text
            user_msg = None
            cont += 1

        else:  # esse else vai virar outra coisa
            print('h')
            time.sleep(5)
            last_text = text
    except Exception:
        try:
            while True:
                play = msg_user[last].find_element_by_class_name('_1h3dW').click()
                time.sleep(15)
                if os.path.exists("C:\\Users\\NOME DO DIRETÓRIO\\speech_recognition.txt"):
                    print('audio')
                    # Localizando o arquivo a ser lido com as conversas escutadas e salvando a ultima linha em uma variável
                    for escuta in os.listdir("C:\\Users\\NOME DO DIRETÓRIO\\IA"):
                        if (escuta == "speech_recognition.txt"):
                            escuta_e = open("C:\\Users\\NOME DO DIRETÓRIO\\IA" + '\\' + escuta, 'r',
                                            encoding='utf-8')
                            escuta_e_op = escuta_e.readlines()
                            qnt_escuta_e = len(escuta_e_op) - 1
                            last_escuta_e = escuta_e_op[qnt_escuta_e]
                            print(last_escuta_e)

                            resp = bot.get_response(last_escuta_e)
                            resp = str(resp)
                            msg_box.send_keys(resp)  # vai digitar
                            time.sleep(2)
                            driver.find_element_by_class_name('_3M-N-').click()  # botão de enviar

                            msg_user = driver.find_elements_by_class_name(
                                '_1zGQT')  # vai pegar a proria mensagem enviada
                            last = len(msg_user) - 1
                            text = msg_user[last].find_element_by_css_selector(
                                'span.selectable-text').text  # vai pegar a propria mensagem enviada
                            last_text = text
                            cont += 1
                            break
                    break
                else:
                    time.sleep(5)
        except Exception:
            list_err = ['Quer me bugar?', 'Kkkj', 'Tô de boa xd', 'hm', '?','????', 'fds', 'fodase']
            alt_num = random.randint(0, 4)  # numero aleatório
            msg_box.send_keys(list_err[alt_num])
            time.sleep(2)
            driver.find_element_by_class_name('_3M-N-').click()  # botão de enviar

            msg_user = driver.find_elements_by_class_name('_1zGQT')  # vai pegar a proria mensagem enviada
            last = len(msg_user) - 1
            text = msg_user[last].find_element_by_css_selector(
                'span.selectable-text').text  # vai pegar a propria mensagem enviada
            last_text = text
            user_msg = None
            cont += 1
