car_makers = {'Acura':'Japan','Fiat':'Egypt'}
car_makers.update({'Tesla':'USA'})
car_makers['Fiat'] = 'Italy'
print'Acura made in',car_makers['Acura']
print'Fiat made in',car_makers['Fiat']
print'Tesla made in',car_makers['Tesla']