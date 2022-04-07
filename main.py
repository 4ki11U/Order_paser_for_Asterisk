#!/usr/bin/python3
from requests_ntlm import HttpNtlmAuth
from requests import Session
from zeep import Client
from zeep.transports import Transport
from xml.etree import ElementTree
from sys import argv
import re

session = Session()
session.auth = HttpNtlmAuth('login', 'password')
client = Client('http://url_for_connect', transport=Transport(session=session))

caller = argv[1]  # номер звонящего, который мы ловим с астериска как $caller

body = f'''
        <Request>
        <Request_ID>CUSTOMER_ORDER_FILTERED_LIST</Request_ID>
        <Request_Body>
        <Include_Posted_Customer_Orders>yes</Include_Posted_Customer_Orders>
        <Customer_Order_Header>
        <Document_Id></Document_Id>
        <Store_No.></Store_No.>
        <Created_at_Store></Created_at_Store>
        <Document_DateTime>2021-11-28T00:00:00.000Z</Document_DateTime>
        <Member_Contact_No.></Member_Contact_No.>
        <Member_Contact_Name></Member_Contact_Name>
        <Inventory_Transfer>0</Inventory_Transfer>
        <Full_Name></Full_Name>
        <Address></Address>
        <Phone_No.>{caller}</Phone_No.>
        <Email></Email>
        <Member_Card_No.></Member_Card_No.>
        </Customer_Order_Header>
        </Request_Body>
        </Request>
        '''.encode('utf-8')

data = client.service.WebRequest(body, '?').pxmlResponse


def find_id():

	root2 = ElementTree.XML(data)
	dictionary = dict()

	for element in root2:
		if element.tag == 'Response_Body':
			for i in element:
				Delivery_Order_Status = None
				document_id = None
				for j in i:
					if j.tag == 'Delivery_Order_Status':
						Delivery_Order_Status = j.text
						print(Delivery_Order_Status)
					elif j.tag == 'Document_Id':
						document_id = j.text
				if Delivery_Order_Status in dictionary:
					order = dictionary[f'{Delivery_Order_Status}']
					member_of_order = order.append(f'{document_id}')
				else:
					dictionary[f'{Delivery_Order_Status}'] = [f'{document_id}']
	playback(dictionary)


def deleting_nulls_in_order(nomer):

	ishem_nyli = re.match(r'^00', nomer)

	if ishem_nyli is None:
		removed = re.sub(r'^(0)', r'\1 ', nomer)
	else:
		removed = re.sub(r'^(0)(0)', r'\1 \2 ', nomer)
	return removed.split(" ")


def playback(dictionary):

	our_keys = list(dictionary.keys())

	if '0' in our_keys or '1' in our_keys or '2' in our_keys:
		print('EXEC PLAYBACK za_vashym_nomerom_new')

	for key, value in dictionary.items():
		if key == '0':
			for nomer_zakaza in value:
				print(f'status_info is Open({key})')
				print(f'EXEC PLAYBACK vash_zakaz_nomer')
				bykvi_zakaza = nomer_zakaza[0:2]
				result_of_chistki_nyley1 = deleting_nulls_in_order(nomer_zakaza[2:5])
				print(f'EXEC SayAlpha {bykvi_zakaza}')
				for i in result_of_chistki_nyley1:
					print(f'EXEC SayNumber {i}')
				result_of_chistki_nyley2 = deleting_nulls_in_order(nomer_zakaza[5:8])
				for i in result_of_chistki_nyley2:
					print(f'EXEC SayNumber {i}')
			print(f'EXEC PLAYBACK na_opracuvanni')

		if key == '1':
			for nomer_zakaza in value:
				print(f'status_info is Released({key})')
				print(f'EXEC PLAYBACK vash_zakaz_nomer')
				bykvi_zakaza = nomer_zakaza[0:2]
				result_of_chistki_nyley1 = deleting_nulls_in_order(nomer_zakaza[2:5])
				print(f'EXEC SayAlpha {bykvi_zakaza}')
				for i in result_of_chistki_nyley1:
					print(f'EXEC SayNumber {i}')
				result_of_chistki_nyley2 = deleting_nulls_in_order(nomer_zakaza[5:8])
				for i in result_of_chistki_nyley2:
					print(f'EXEC SayNumber {i}')
			print(f'EXEC PLAYBACK na_opracuvanni')

			if key == '2':
				for nomer_zakaza in value:
					print(f'status_info is Shipped({key})')
					print(f'EXEC PLAYBACK vash_zakaz_nomer')
					bykvi_zakaza = nomer_zakaza[0:2]
					result_of_chistki_nyley1 = deleting_nulls_in_order(nomer_zakaza[2:5])
					print(f'EXEC SayAlpha {bykvi_zakaza}')
					for i in result_of_chistki_nyley1:
						print(f'EXEC SayNumber {i}')
					result_of_chistki_nyley2 = deleting_nulls_in_order(nomer_zakaza[5:8])
					for i in result_of_chistki_nyley2:
						print(f'EXEC SayNumber {i}')
				print(f'EXEC PLAYBACK vidvantazhene')


if __name__ == '__main__':
	find_id()
