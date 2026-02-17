========================  10  ========================


Задание 10
Магазин обслуживает покупателей. В магазине работает 4 продавца. Необходимо определить выручку, которую получит магазин в конце рабочего дня. Известно, что каждый покупатель в среднем делает покупки на 200 р. Продавец обслуживает покупателя (153 минуты), затем выбивает чек и снова начинает обслуживание покупателей. 


Измените количество продавцов (пусть их будет 6). Как изменятся результаты?

~~~

FACILITY         ENTRIES  UTIL.   AVE. TIME AVAIL. OWNER PEND INTER RETRY DELAY
 KASSA               87    0.898       4.957  1        1    0    0     0      0


FACILITY         ENTRIES  UTIL.   AVE. TIME AVAIL. OWNER PEND INTER RETRY DELAY
 KASSA               94    0.974       4.973  1        3    0    0     0      3

~~~


Магазин обслуживает покупателей. Покупатели появляются в магазине каждые 30+-10 минуты. Обслуживают покупателей продавец и кассир. Время обслуживания 
продавцом составляет 20 минут, а кассиром – 7+-3 минуты. Если продавец видит, что количество покупателей растёт, интенсивность его работы увеличивается 
на величину, равную длине средней длине очереди. Из предыдущих примеров моделирования стало ясно, что один продавец не справляется с обслуживанием потока посетителей.
Администрация решила нанять на работу ещё одного продавца. Таким образом, как только посетитель приходит в магазин он с равной вероятность может быть обслужен как 
одним, так и другим продавцом. Второй продавец работает с той же интенсивностью, что и первый, а когда видит, что очередь посетителей большая, то и его 
интенсивность увеличивается, но  на величину, равную максимальной длине очереди.
1. Определить, какова средняя и максимальная длины очередей в магазине, если моделирование выполняется в течение 8 часов. 
      Определить среднее время пребывания клиента в очереди к кассиру и каждому из продавцов.
2. Измените интенсивность работы кассиров, предположите, что время обслуживания кассиром уменьшается по 
      сравнению с прежним значением на 50% от среднего времени пребывания клиента в очереди.

========================  11.1  ========================
SELLER1_INTENSIVITY VARIABLE 20-QA$QSELLER              
SELLER2_INTENSIVITY VARIABLE 20-QM$QSELLER                 

GENERATE 30,10
      QUEUE QSELLER
      TRANSFER 0.5,SERVSELLER1,SERVSELLER2
SERVSELLER1   SEIZE SELLER
      DEPART QSELLER
      ADVANCE V$SELLER1_INTENSIVITY                         
      RELEASE SELLER
      TRANSFER ,Res
SERVSELLER2   SEIZE SELLER2
      DEPART QSELLER
      ADVANCE V$SELLER2_INTENSIVITY                      
      RELEASE SELLER2
Res   QUEUE QKASSA
      SEIZE KASSA
      DEPART QKASSA
      ADVANCE 7,3
      RELEASE KASSA
      TERMINATE
      
GENERATE 480
      TERMINATE 1
      
START 1


========================    ========================
FACILITY         ENTRIES  UTIL.   AVE. TIME AVAIL. OWNER PEND INTER RETRY DELAY
 SELLER2              7    0.277      19.000  1        0    0    0     0      0
 KASSA               16    0.242       7.250  1       17    0    0     0      0
 SELLER               9    0.375      20.000  1        0    0    0     0      0


QUEUE              MAX CONT. ENTRY ENTRY(0) AVE.CONT. AVE.TIME   AVE.(-0) RETRY
 QSELLER             1    0     16     16     0.000      0.000      0.000   0
 QKASSA              1    0     16     16     0.000      0.000      0.000   0


СРЕДНЕЕ И МАКСИМАЛЬНОЕ В ОЧЕРЕДИ 0


========================  11.2  ========================
SELLER1_INTENSIVITY VARIABLE 20-QA$QSELLER              
SELLER1_INTENSIVITY VARIABLE 20-QA$QSELLER#0.5

FACILITY         ENTRIES  UTIL.   AVE. TIME AVAIL. OWNER PEND INTER RETRY DELAY
 SELLER2              7    0.277      19.000  1        0    0    0     0      0
 KASSA               16    0.242       7.250  1       17    0    0     0      0
 SELLER               9    0.375      20.000  1        0    0    0     0      0


QUEUE              MAX CONT. ENTRY ENTRY(0) AVE.CONT. AVE.TIME   AVE.(-0) RETRY
 QSELLER             1    0     16     16     0.000      0.000      0.000   0
 QKASSA              1    0     16     16     0.000      0.000      0.000   0

НЕТ РАЗНИЦЫ


Магазин обслуживает покупателей. Покупатели появляются в магазине каждые 30+-10 минуты. Обслуживают покупателей продавец и кассир. Время обслуживания 
продавцом составляет 12+ n минуты (интенсивность работы снижается к вечеру от усталости, чем большее количество клиентов было обслужено, тем меньше интенсивность, тем больше время обслуживания. Пусть время обслуживания растёт на 20 процентов от количества клиентов, т.о. n = FC$seller#0.2), а кассиром - 72.  Через 6 часа после начала работы появляется новый поток посетителей (рабочие и служащие, завершившие работу), интервалы между приходами этих посетителей - 72 минуты. 
Добавьте второго продавца, пусть время обслуживания клиентов вторым продавцом зависит от числа входов покупателей в очередь (25% от этого значения).

1. Измените интенсивность работы второго продавца, и посмотрите, как это скажется на длине очереди.

2. Добавьте второго кассира для работы в вечернее время.

3. Измените условия задачи: пусть интенсивность работы кассира увеличивается на 10 процентов от FR,FT и FC.



========================  12.1  ========================

SELLER1_INTENSIVITY VARIABLE 12+FC$seller#0.2                ; 12+{количествоВходовВУстройствоSeller}*0.2
SELLER2_INTENSIVITY VARIABLE QC$QSELLER#0.25                 ; входыВОчередь*0.25
KASS_INTENSIVITY VARIABLE 7-FC$KASSA#0.1-FT$KASSA#0.1        ; 7-входыВКассу*0.1-среднееВремяВОчереди*0.1

GENERATE 30,10
      QUEUE QSELLER
      TRANSFER 0.5,SERVSELLER1,SERVSELLER2
SERVSELLER1   SEIZE SELLER
      DEPART QSELLER
      ADVANCE V$SELLER1_INTENSIVITY                          ;Обращаемся к переменной SELLER1_INTENSIVITY
      RELEASE SELLER
      TRANSFER ,Res
SERVSELLER2   SEIZE SELLER2
      DEPART QSELLER
      ADVANCE (QC$QSELLER#0.25)                         ;обслуживание длится входыВОчередь*0.25
      RELEASE SELLER2
Res   QUEUE QKASSA
      SEIZE KASSA
      DEPART QKASSA
      ADVANCE V$KASS_INTENSIVITY
      RELEASE KASSA
      TERMINATE
      
GENERATE 7,2,360
      QUEUE QSELLER
      TRANSFER 0.5,SERVNSELLER1,SERVNSELLER2
SERVNSELLER1   SEIZE SELLER
      DEPART QSELLER
      ADVANCE V$SELLER1_INTENSIVITY
      RELEASE SELLER
      TRANSFER ,Res2
SERVNSELLER2   SEIZE SELLER2
      DEPART QSELLER
      ADVANCE V$SELLER2_INTENSIVITY
      RELEASE SELLER2
Res2  QUEUE QKASSA
      SEIZE KASSA
      DEPART QKASSA
      ADVANCE V$KASS_INTENSIVITY
      RELEASE KASSA
      TERMINATE
      
GENERATE 720
      TERMINATE 1
      
START 1

========================        ========================

FACILITY         ENTRIES  UTIL.   AVE. TIME AVAIL. OWNER PEND INTER RETRY DELAY
 SELLER2             41    0.453       7.954  1       68    0    0     0      7
 KASSA               64    0.294       3.302  1        0    0    0     0      0
 SELLER              25    0.487      14.035  1       66    0    0     0      3


QUEUE              MAX CONT. ENTRY ENTRY(0) AVE.CONT. AVE.TIME   AVE.(-0) RETRY
 QSELLER            11   10     76     24     1.476     13.979     20.431   0
 QKASSA              1    0     64     50     0.053      0.599      2.736   0



SELLER2_INTENSIVITY VARIABLE QC$QSELLER#0.25                 
SELLER2_INTENSIVITY VARIABLE QC$QSELLER#0.5                 

FACILITY         ENTRIES  UTIL.   AVE. TIME AVAIL. OWNER PEND INTER RETRY DELAY
 SELLER2             31    0.488      11.329  1       48    0    0     0     17
 KASSA               54    0.284       3.784  1        0    0    0     0      0
 SELLER              25    0.487      14.035  1       66    0    0     0      3


QUEUE              MAX CONT. ENTRY ENTRY(0) AVE.CONT. AVE.TIME   AVE.(-0) RETRY
 QSELLER            21   20     76     22     3.885     36.803     51.797   0
 QKASSA              2    0     54     47     0.025      0.335      2.587   0

========================  12.2  ========================


SELLER1_INTENSIVITY VARIABLE 12+FC$seller#0.2                ; 12+{количествоВходовВУстройствоSeller}*0.2
SELLER2_INTENSIVITY VARIABLE QC$QSELLER#0.25                 ; входыВОчередь*0.25
KASS_INTENSIVITY VARIABLE 7-FC$KASSA#0.1-FT$KASSA#0.1        ; 7-входыВКассу*0.1-среднееВремяВОчереди*0.1

GENERATE 30,10
      QUEUE QSELLER
      TRANSFER 0.5,SERVSELLER1,SERVSELLER2
SERVSELLER1   SEIZE SELLER
      DEPART QSELLER
      ADVANCE V$SELLER1_INTENSIVITY                          ;Обращаемся к переменной SELLER1_INTENSIVITY
      RELEASE SELLER
      TRANSFER ,Res
SERVSELLER2   SEIZE SELLER2
      DEPART QSELLER
      ADVANCE (QC$QSELLER#0.25)                         ;обслуживание длится входыВОчередь*0.25
      RELEASE SELLER2
Res   QUEUE QKASSA
      SEIZE KASSA
      DEPART QKASSA
      ADVANCE V$KASS_INTENSIVITY
      RELEASE KASSA
      TERMINATE
      
GENERATE 7,2,360
      QUEUE QSELLER
      TRANSFER 0.5,SERVNSELLER1,SERVNSELLER2
SERVNSELLER1   SEIZE SELLER
      DEPART QSELLER
      ADVANCE V$SELLER1_INTENSIVITY
      RELEASE SELLER
      TRANSFER ,Res2
SERVNSELLER2   SEIZE SELLER2
      DEPART QSELLER
      ADVANCE V$SELLER2_INTENSIVITY
      RELEASE SELLER2
Res2  TRANSFER 0.5,SERVKASSA1,SERVKASSA2
SERVKASSA1  QUEUE QKASSA
      SEIZE KASSA
      DEPART QKASSA
      ADVANCE V$KASS_INTENSIVITY
      RELEASE KASSA
      TRANSFER ,TERM
SERVKASSA2  QUEUE QKASSA
      SEIZE KASSA2
      DEPART QKASSA
      ADVANCE V$KASS_INTENSIVITY
      RELEASE KASSA2
      TRANSFER ,TERM
TERM  TERMINATE
      
GENERATE 720
      TERMINATE 1
      
START 1

========================        ========================

FACILITY         ENTRIES  UTIL.   AVE. TIME AVAIL. OWNER PEND INTER RETRY DELAY
 SELLER2             39    0.438       8.080  1       71    0    0     0      5
 KASSA               44    0.261       4.268  1        0    0    0     0      0
 SELLER              27    0.548      14.616  1       63    0    0     0      7
 KASSA2              20    0.094       3.381  1       68    0    0     0      0


QUEUE              MAX CONT. ENTRY ENTRY(0) AVE.CONT. AVE.TIME   AVE.(-0) RETRY
 QSELLER            13   12     78     22     1.955     18.048     25.138   0
 QKASSA              1    0     64     57     0.015      0.169      1.548   0


========================  12.3  ========================

KASS_INTENSIVITY VARIABLE 7-FC$KASSA#0.1-FR$KASSA#0.1

02/17/26 19:58:46  Halt. XN: 4. Block 16 Next. 
02/17/26 19:58:46    Clock:72.901660. Next: ADVANCE. Line 20. 
02/17/26 19:58:46        ADVANCE V$KASS_INTENSIVITY
02/17/26 19:58:46    Negative time increment.

========================    ========================

KASS_INTENSIVITY VARIABLE 7-FC$KASSA#0.1-FT$KASSA#0.1

FACILITY         ENTRIES  UTIL.   AVE. TIME AVAIL. OWNER PEND INTER RETRY DELAY
 SELLER2             41    0.453       7.954  1       68    0    0     0      7
 KASSA               64    0.294       3.302  1        0    0    0     0      0
 SELLER              25    0.487      14.035  1       66    0    0     0      3


QUEUE              MAX CONT. ENTRY ENTRY(0) AVE.CONT. AVE.TIME   AVE.(-0) RETRY
 QSELLER            11   10     76     24     1.476     13.979     20.431   0
 QKASSA              1    0     64     50     0.053      0.599      2.736   0


========================    ========================

KASS_INTENSIVITY VARIABLE 7-FC$KASSA#0.1-FC$KASSA#0.1

02/17/26 20:04:33  Halt. XN: 38. Block 34 Next. 
02/17/26 20:04:33    Clock:508.655908. Next: ADVANCE. Line 39. 
02/17/26 20:04:33        ADVANCE V$KASS_INTENSIVITY
02/17/26 20:04:33    Negative time increment.



