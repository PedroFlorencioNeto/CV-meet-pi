# Projeto Conheça o Pi - Movimentação do Mouse
# Autor: Pedro Florencio de Almeida Neto - pedroflorencio@alu.ufc.br

# -----------------------------------------------------------------------------------------------------------#
# Bibliotecas 
import cv2
import mediapipe
import numpy
import pyautogui
# -----------------------------------------------------------------------------------------------------------#

cap = cv2.VideoCapture(0) # Inicia captura da webcam

initHand = mediapipe.solutions.hands  # Inicialização do MediaPipe

# Adiciona alguns argumentos ao módulo como: Quantidade de mãos que vamos usar, Grau de confiança no rastreamento
mainHand = initHand.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.8)

draw = mediapipe.solutions.drawing_utils  # Desenha as conexões dos dedos e seus respectivos índices

wScr, hScr = pyautogui.size()  # Retorna largura e comprimento da tela

pX, pY = 0, 0  # Localização anterior de x e y
cX, cY = 0, 0  # Localização atual de x e y



def handLandmarks(colorImg):
    landmarkList = []  # Inicializa os valores

    landmarkPositions = mainHand.process(colorImg)  # Processamento do vídeo de entrada
    landmarkCheck = landmarkPositions.multi_hand_landmarks  # Armazena a saída do processamento (retorna False on empty) Verifica se está rastreando
    if landmarkCheck:  # Checa se os pontos de referência estão mapeados
        for hand in landmarkCheck:  # Pontos de referência para cada mão
            for index, landmark in enumerate(hand.landmark):  # Faz um loop pelos 21 índices e produz suas coordenadas de referência (x, y, & z)
                draw.draw_landmarks(img, hand, initHand.HAND_CONNECTIONS)  # Desenha cada índice e suas conexões
                h, w, c = img.shape  # altura, largura e canal da imagem
                centerX, centerY = int(landmark.x * w), int(landmark.y * h)  # Converte as coordenadas decimais relativas à imagem para cada índice
                landmarkList.append([index, centerX, centerY])  # Adiciona os índices e suas coordenadas em uma lista
                
    return landmarkList


def fingers(landmarks):
    fingerTips = []  # Armazena 4 conjuntos de 1s e 0s
    tipIds = [4, 8, 12, 16, 20]  # Índices das pontas dos dedos
    
    # Verifica se o polegar está para cima
    if landmarks[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
        fingerTips.append(1)
    else:
        fingerTips.append(0)
    
    # Verifica se os outros dedos estão para cima
    for id in range(1, 5):
        if landmarks[tipIds[id]][2] < landmarks[tipIds[id] - 3][2]:  # Verifica se cada ponta do dedo é maior que as suas juntas 
            fingerTips.append(1)
        else:
            fingerTips.append(0)

    return fingerTips

# Loop infinito
while True:
    check, img = cap.read()  # Lê os quadros da câmera
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Converte BGR para RGB
    lmList = handLandmarks(imgRGB)
    # cv2.rectangle(img, (75, 75), (640 - 75, 480 - 75), (255, 0, 255), 2)
    
    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]  # Pega os valores de x e y do índice 8
        x2, y2 = lmList[12][1:]  # Pega os valores de x e y do índice 12
        finger = fingers(lmList)  # Verifica quais dedos estão para cima
        
        if finger[1] == 1 and finger[2] == 0:  # Se o indicador estiver levantado e o polegar não
            x3 = numpy.interp(x1, (75, 640 - 75), (0, wScr))  # Converte a largura da janela em relação à largura da tela
            y3 = numpy.interp(y1, (75, 480 - 75), (0, hScr))  # Converte a altura da janela em relação à altura da tela
            
            cX = pX + (x3 - pX) / 20  # Armazena x localizações anteriores para atualizar x localização atual
            cY = pY + (y3 - pY) / 20  # Armazena y localizações anteriores para atualizar y localização atual
            
            pyautogui.moveTo(wScr-cX, cY)  # Função que move o mouse para os valores x3 e y3  (wSrc inverte a direção)
            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
            pX, pY = cX, cY  # Armazena a localização atual de x e y como localização x e y anterior para o próximo loop

        if finger[1] == 0 and finger[0] == 1:  # Se o polegar tiver levantado e o indicador abaixado, clique com o notão esquerdo
            pyautogui.click()  # Clique com o botão esquerdo
            
    cv2.imshow("Webcam", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

