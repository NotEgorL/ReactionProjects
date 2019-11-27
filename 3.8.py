import pygame, sys, time, random
import statistics as st
#setup------------------------------------------------------------------------------------------
pygame.init()
screen = pygame.display.set_mode([800,450])
pygame.display.set_caption("Reaction game")

#colours ---------------------------------------------------------------------------------------
white, red, black, green, blue = [255, 255, 255], [255, 0, 0], [0, 0, 0],[0, 255, 0],[0, 0, 255]
listColours=[red, blue, green, black]
screen.fill(white)              #start with a white screen
pygame.display.update()

#text+fonts-------------------------------------------------------------------------------------
fontOfText=pygame.font.SysFont("times New Roman",20)
singleText=fontOfText.render(u"Ваш Результат по прошлому нажжатию",1,black)
meanText=fontOfText.render(u"Ваш Общий Результат За Весь Пробег",1,black)


resultsList=[]
#10 rounds of random delay flashes. click to secure time


for i in range(10):
    time.sleep(random.randint(1,3))
    done=False
    screen.fill(random.choice(listColours))
    pygame.display.update()
    start=time.time()
    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                done= True
    end=time.time()

#results calculation. is acted on 10 times
    res=round(end-start,10)
    resultsList.append(res)

#var texts--------------------------------------------------------------------------------------
    singleResult=fontOfText.render(str(res),1,black)
    meanResult=fontOfText.render(str(st.mean(resultsList)),1,black)
    screen.fill(white)
    screen.blit(singleText,(0,0))
    screen.blit(meanText,(0,30))
    screen.blit(singleResult,(400,0))
    screen.blit(meanResult,(400,30))
    
    pygame.display.update()
   

print("Overall average is:  ",st.mean(resultsList))

    
    
