# Python_basic_diploma
## ��������. �������� ���: "������� ���".
�������� ��� ��� ���, ��� ����� ����� ������ �� ������������ ���������.<br/>
� ������ ���� ����� ���� �� ������� ���������: ��� � ����.
� ����� �� �������������� ����������, ����� ���: �� ������� ������ ������ ������, �� ������� �������� ������, 
�� ������� ������ ������������ � �� ������� �������� ������ � ������.

����� ����� ����, ����� ��������� � �������� API �����<br/> https://api-ninjas.com/api/dogs

### ������ ���������
������ ���������� �� ����� Python, � ����������� � ������� ������������ ����������� � ��������� �����������
��������� (pip install -r requirements.txt).<br/>

��� ������� ���������� �������� *"api ����"* �� ����� https://api-ninjas.com/api <br/>
� ����� ��������-����. ��� �������� ����� ����� ������ �� ������ https://core.telegram.org/api  <br/>
����� ��������� ������, ����������� �� � �������� � ���� *.env* � �������� ����� �������.
```
TOKEN_TG = '�������� �����'
API_key = 'api ���� �����'
```
��� ����������� �� ����� ***main.py***, ������������ � �������� ����� �������.

### ������������ ������������ � �����
������������ ����� ��������������� � ����� ����� ������� � ���� ���������� ��� �� ���� ����.<br/>
������ ������, ������� ������������ ����� ������������:

1. /start - ������ ����
2. /help - �������� ������
3. /history - ����� ������� ������ (��������� ������ ��������)
4. /low - ����� ������ ����� �� ����������� ���������: ���� � �����, � ������������ ������ �������������� ���������� (��. ��������)
5. /high - ����� ������ ����� �� ������������ ���������: ���� � �����, � ������������ ������ �������������� ���������� (��. ��������)
6. /custom - ����� ����������� ����������������� ��������� �� ��������� ���� � ����� ������


#### ������� /low, /high � /custom ��������� �������� ����������:
* ����������� ���
* ������������ ���
* ����������� ����
* ������������ ����
* ����������������� ����� (�� � ��)
* ����������� ������

� ����� �� ������� �� ����������� ����� ������:
* ������
* ����� (�������)
* ��������� (����������� � �����������)
* ����������� ������ � ������
* ������������� � ������
* ������������� � ������� ��������
* ������������ ������

### ����� �������
**database** - �������� ������ ��� ������ � ����� ������.
��������������� � �������� /history, ��� ��������� ������� ������.

**siteAPI** - �������� ����� � ��������� �� ������� ���� ������ � ����� Api ��� ������:
1. ***dog_finder.py*** ��� �������� �� �������� /low � /high
2. ***cust_req.py*** ��� ������� �� ������� /custom

**tgAPI** - �������� ���������� ����������, ������ ������ ��������� � ���, ��� ������ ��������-����