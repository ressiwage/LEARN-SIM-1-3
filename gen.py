seller=input('seller (def 12,2): ')
casher = input('casher (def 7,2): ')

print(f"""
GENERATE  30,10                ;Новый посетитель
QUEUE     QSELLER             ;Постановка в очередь
SEIZE     SELLER              ;Начать обслуживание или          ожидать в очереди, когда продавец освободится
DEPART    QSELLER             ;Выход из очереди
ADVANCE   {seller}                ;Обслуживание покупателя
RELEASE   SELLER              ;Завершение обслуживания
QUEUE     QKASSA              ;Постановка в очередь
SEIZE     KASSA               ;Начать обслуживание или          ожидать в очереди, когда кассир освободится
DEPART    QKASSA              ;Выход из очереди
ADVANCE   {casher}                ;Обслуживание покупателя
RELEASE   KASSA              ;Завершение обслуживания
TERMINATE

GENERATE  7,2,360                ;Новый посетитель
QUEUE     QSELLER             ;Постановка в очередь
SEIZE     SELLER              ;Начать обслуживание или          ожидать в очереди, когда продавец освободится
DEPART    QSELLER             ;Выход из очереди
ADVANCE   {seller}                ;Обслуживание покупателя
RELEASE   SELLER              ;Завершение обслуживания
QUEUE     QKASSA              ;Постановка в очередь
SEIZE     KASSA               ;Начать обслуживание или          ожидать в очереди, когда кассир освободится
DEPART    QKASSA              ;Выход из очереди
ADVANCE   {casher}                ;Обслуживание покупателя
RELEASE   KASSA              ;Завершение обслуживания
TERMINATE
                            
                                
GENERATE  480
TERMINATE 1
START 1      
""")