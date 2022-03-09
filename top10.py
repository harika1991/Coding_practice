def return_value(item):
        return item[1]

with open("/Users/haritk/Desktop/text.txt",'r') as f:
        ip_address = {}
        for line in f:
                t=line.split(',')
                ip=t[-1].strip('\n')
                if ip in ip_address:
                        ip_address[ip]+=1
                else:
                        ip_address[ip]=1
        ip_sort=sorted(ip_address.items(), key=lambda A:A[1], reverse=True)
        print ip_sort
        print(ip_address.items())

        print(ip_sort[:2])
        top_2_ip = ip_sort[:2]

        for i, j in enumerate(top_2_ip):
                print str(i+1) +','+j[0]+','+str(j[1])
