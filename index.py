import io
import re
def writeFileLine(filename, nd_line):
	f = open(filename, "a")
	f.write(nd_line + '\n')
	f.close()
def writeUtf8(filename,nd_line):
    f = io.open(filename, mode="a", encoding="utf-8")
    # f.writelines("")
    f.write(nd_line + '\n')
    f.close()

nd_line="vendor_guid,object_type,title,description,display_name,calculation_method,calculation_int,workflow_state,parent_guids,ratings"
writeUtf8('kq.txt',nd_line)

chars=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
f = io.open("Learning Outcomes.txt", mode="r", encoding="utf-8")
list_lines=f.readlines()
#print(len(list_lines))
#read file line by line
current_group=''
for line in list_lines:
    #print(line)
    #check danh muc pattern: number.number
    kq1=re.search(r'(((\d)+\.)+\d)',line)
    #check danh muc pattern:number
    kq2=re.search(r'( \d )',line)
    
    
    
    #1.1  KIẾN THỨC TOÁN HỌC VÀ KHOA HỌC CƠ BẢN
    if kq1!=None:
        #print('TH_a')
        id=kq1.group(1)
        type='group'
        parent='.'.join(id.split('.')[:-1])

        current_group=id #outcome dua vao de lay parent
        current_id=id #outcome dua vao de lay id =>1.2.3
        index_char=0 #outcome dua vao de lay id => a,b,c
        
    
    #1  KIẾN THỨC VÀ LẬP LUẬN NGÀNH
    elif kq1==None and kq2!=None and line.isupper():
        #print('TH_b')
        id=kq2.group(1)
        type='group'
        parent=''
        
    elif kq1==None and kq2==None and line.isupper()==False:
        #print('TH_c')
        char=chars[index_char]
        index_char+=1
        id='%s_%s'%(current_id,char)
        type='outcome'
        parent=current_group

    name=line
    name=line.replace('\r','').replace('\t','').replace('   ','')
    name=name.replace(" ",' ')
    name=name.replace(",",'__COMMA__')
    name=name.replace(id,'')

    name=''.join(e for e in name if e.isalnum() or e==" " or e=="(" or e==")" or e=="{" or e=="}" or e=='_')

    print("line:",line)
    print("id:",id)
    print("type:",type)
    print("parent:",parent)
    print("name:",name)
    #input('------------------------------------------------')
    #print('------------------------------------------------')
    nd_line="%s,%s,%s,%s,%s,%s,%s,%s,%s,%s"%(id,type,name,'',id,'','','',parent,'')
    #nd_line="vendor_guid,object_type,title,description,display_name,calculation_method,calculation_int,workflow_state,parent_guids,ratings"

    
    writeUtf8('kq.txt',nd_line)
f.close()