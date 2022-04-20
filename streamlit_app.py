import pdfkit
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
from datetime import date
import streamlit as st
import streamlit_authenticator as stauth
from streamlit.components.v1 import iframe


def period_counter(list1,list4,n):
    index = list1.index(n)
    per=list4[index]
    return per


newhtml="""
            <!DOCTYPE html>
            <header></header>
            <style>
               .css-1v3fvcr{background: rgb(34,193,195);
                background: radial-gradient(circle, rgba(34,193,195,1) 46%, rgba(229,229,184,1) 100%);
                }
                div.css-nlntq9.e16nr0p33 p{background-color:white;
                }
                .css-nlntq9.e16nr0p33{}
                .block-container.css-12oz5g7.egzxvld2{background-color:white;
                    border:5px solid orange;
                    border-radius:15px;
                    margin-top:67px;
                }
                .css-6awftf.e19lei0e1{ display:none;}

                .title{}
                .css-1cpxqw2.edgvbvh5{background-color:orange;
                    color: white;
                }
                .css-1cpxqw2.edgvbvh5:focus{background-color:white;
                    color: orange;
                    font-weight:bold;
                    border:3px solid orange;

                }
            
            </style>
            <body> 
            </body
        """
st.markdown(newhtml,unsafe_allow_html=True)


names = ['MARIA	TERZI','Στεριανή Αβράμη','ΔΕΣΠΟΙΝΑ ΑΒΡΑΜΙΔΟΥ','Μαρία Αγάθου']
usernames = ['Maria-terzi@hotmail.com','stella-a88@hotmail.com','depi1970@hotmail.com','magathou@hotmail.com']
passwords = ['tSYcA8GPCJ','hj2cJpZLXG','u46UXerHf9','pJH9CA7L2g']

html_logo = "<img style='display:block; margin-left:auto; margin-right:auto; text-align:center;' src='http://inclusiveeducation.eu/wp-content/uploads/2021/03/logoiam400x400.png'  width=300 height=300>"



st.markdown(html_logo, unsafe_allow_html=True)

# names = ['ΛΑΜΠΡΙΑΝΑ ΤΣΙΑΚΠΙΝΗ','ΜΑΡΙΑ-ΕΙΡΗΝΗ ΓΑΛΕΡΑΚΗ','ΚΟΥΛΑ ΑΜΠΕΛΙΟΤΗ','ΕΙΡΗΝΗ ΑΝΑΤΣΟΥΤΣΟΥΛΑ','ΤΑΤΙΑΝΑ ΕΛΕΟΝΩΡΑ ΑΝΑΓΝΩΣΤΙΔΟΥ','ΕΥΓΕΝΙΑ ΤΡΑΓΑΚΗ','ΣΠΥΡΙΔΩΝ ΒΑΛΒΗΣ','ΣΟΦΙΑ ΓΙΔΑΡΗ','ΔΗΜΗΤΡΗΣ ΑΡΒΑΝΙΤΗΣ','ΠΑΝΑΓΙΩΤΑ ΒΑΣΙΛΕΙΟΥ','ΕΜΜΑΝΟΥΕΛΑ ΒΑΣΙΛΕΙΑΔΗ','ΜΑΡΙΑ ΓΟΥΡΓΙΩΤΗ','ΕΛΠΙΔΑ ΓΟΥΚΟΥ','ΜΑΡΙΑ ΤΕΡΖΟΥΔΗ','ΓΕΩΡΓΙΑ ΒΕΛΟΥΔΟΥ','ΜΑΡΙΑ ΤΕΡΖΗ','ΜΑΡΙΑ ΓΕΩΡΓΟΠΟΥΛΟΥ','ΒΑΣΣΟ ΑΝΔΡΟΥΤΣΟΥ','ΧΡΗΣΤΙΝΑ ΑΛΒΑΝΗ','ΘΕΟΔΩΡΑ ΓΚΟΥΝΑ','ΜΑΡΙΑ ΑΓΑΘΟΥ','ΑΛΕΞΙΟΣ ΑΡΦΑΝΗΣ','ΕΥΑΓΓΕΛΙΑ ΒΑΡΣΑΜΑ','ΧΡΗΣΤΙΝΑ ΒΟΥΛΓΑΡΙΔΟΥ','ΔΕΣΠΟΙΝΑ ΑΒΡΑΜΙΔΟΥ','ΑΛΕΞΑΝΔΡΑ ΑΛΤΙΠΑΡΜΑΚΗ','ΛΟΥΙΖΑ ΑΛΕΞΙΑΔΟΥ','ΒΕΖΑΣΗΣ ΕΥΘΥΜΙΟΣ','ΕΛΛΗ ΑΓΓΕΛΑΚΟΠΟΥΛΟΥ','ΒΑΣΙΛΙΚΗ ΛΑΖΟΥ','ΑΝΔΡΙΑΝΑ ΔΕΛΕΓΚΟΥ','ΑΠΟΣΤΟΛΙΑ ΠΛΙΑΣΣΑ','ΑΝΑΣΤΑΣΙΑ ΧΑΤΖΗΓΕΩΡΓΙΟΥ','ΑΛΙΚΗ ΒΑΒΟΥΓΥΙΟΥ','ΜΕΛΙΝΑ ΑΛΕΞΙΑΔΟΥ','ΤΣΑΡΟΥΧΑΣ ΝΕΚΤΑΡΙΟΣ','ΜΠΟΤΣΩΛΗ ΑΙΚΑΤΕΡΙΝΗ','ΑΙΚΑΤΕΡΙΝΗ ΓΚΑΓΚΑΛΗ','ΔΕΣΠΟΙΝΑ ΧΑΤΖΗΔΡΟΣΟΥ']
 
# usernames = ['labrianatsiak@icloud.com','nikosmariagr@hotmail.com','kampel85@yahoo.gr','spaeirhnh@hotmail.com','tatianapsychology@yahoo.gr','eugenia.tragaki@gmail.com','nsvalv@gmail.com','sofiagidari@yahoo.gr','darv009@hotmail.com','vgiota83@hotmail.com','emmavasi76@gmail.com','maria.gr.bl@hotmail.com','elpidagoukou@yahoo.gr','terzoydi@gmail.com','tzovel72@yahoo.gr','maria-terzi@hotmail.com','mgeorgopoulou@gmail.com','vandrout@yahoo.gr','christina.albani@yahoo.gr','theodoragouna@gmail.com','magathou@hotmail.com','alexiosarfanis@gmail.com','lillyvarsama@yahoo.com','voulgaridou.christina@gmail.com','depi1970@hotmail.com','alexandralt@yahoo.com','louiza.alex@gmail.com','efthymis.v@gmail.com','elliaggel@gmail.com','lazouvaso@yahoo.gr','delegouandriana@yahoo.gr','litsapliassa@gmail.com','anastasiachatz3012@gmail.com','alikakiv_1986@hotmail.com','melinalexiadou@gmail.com','nectsarou@yahoo.gr','botsoli@yahoo.gr','kgkagkali@gmail.com','deppy.h@hotmail.com']

# passwords = ['kKw63vspMq','AV2wPELFZS','BK259LtGwu','a6BzbdXRJu','mLTcrCs6a9','Jv37HCYAMX','j8m7Dn4VHQ','AXJLQHhw7d','ZUc9n2gWVp','Hvuk4aspx7','MLVTdK26SB','UpZcq6hKTC','paT7jEgSAw','eH6ZDwbk2N','Wzp96ykNeD','tSYcA8GPCJ','w3XjgRETsL','Hy26wLYmzk','GsBEYywW9n','TpSe6atkf2','pJH9CA7L2gs','L4UWEuD8MA','Q2GTuYE8ch','xcA43GJWaf','u46UXerHf9','prF4k9VXb2','E8L4MjXsWe','UxYV7bNfv4','Aax5Xe3pTK','X94bWctMj5','TEahK53skD','YFDHf4cB8n','jPsvBFte7z','ZuAf4sPJUw','wWgcxYk7M2','M5Dr8aJxhy','zPeaCyw3nq','j9zVgvyn2w','h6eacUSGrK']


# names=['ΛΑΜΠΡΙΑΝΑ ΤΣΙΑΚΠΙΝΗ', 'ΜΑΡΙΑ - ΕΙΡΗΝΗ ΓΑΛΕΡΑΚΗ', 'ΚΟΥΛΑ ΑΜΠΕΛΙΟΤΗ', 'ΕΙΡΗΝΗ ΑΝΑΤΣΟΥΤΣΟΥΛΑ', 'ΤΑΤΙΑΝΑ ΕΛΕΟΝΩΡΑ ΑΝΑΓΝΩΣΤΙΔΟΥ', 'ΕΥΓΕΝΙΑ ΤΡΑΓΑΚΗ', 'ΣΠΥΡΙΔΩΝ ΒΑΛΒΗΣ', 'ΣΟΦΙΑ ΓΙΔΑΡΗ', 'ΔΗΜΗΤΡΗΣ ΑΡΒΑΝΙΤΗΣ', 'ΠΑΝΑΓΙΩΤΑ ΒΑΣΙΛΕΙΟΥ', 'ΕΜΜΑΝΟΥΕΛΑ ΒΑΣΙΛΕΙΑΔΗ', 'ΜΑΡΙΑ ΓΟΥΡΓΙΩΤΗ', 'ΕΛΠΙΔΑ ΓΟΥΚΟΥ', 'ΜΑΡΙΑ ΤΕΡΖΟΥΔΗ', 'ΓΕΩΡΓΙΑ ΒΕΛΟΥΔΟΥ', 'ΜΑΡΙΑ ΤΕΡΖΗ', 'ΜΑΡΙΑ ΓΕΩΡΓΟΠΟΥΛΟΥ', 'ΒΑΣΣΟ ΑΝΔΡΟΥΤΣΟΥ', 'ΧΡΗΣΤΙΝΑ ΑΛΒΑΝΗ', 'ΘΕΟΔΩΡΑ ΓΚΟΥΝΑ', 'ΜΑΡΙΑ ΑΓΑΘΟΥ', 'ΑΛΕΞΙΟΣ ΑΡΦΑΝΗΣ', 'ΕΥΑΓΓΕΛΙΑ ΒΑΡΣΑΜΑ', 'ΧΡΗΣΤΙΝΑ ΒΟΥΛΓΑΡΙΔΟΥ', 'ΔΕΣΠΟΙΝΑ ΑΒΡΑΜΙΔΟΥ', 'ΑΙΚΑΤΕΡΙΝΗ ΓΚΑΓΚΑΛΗ', 'ΑΛΕΞΑΝΔΡΑ ΑΛΤΙΠΑΡΜΑΚΗ', 'ΛΟΥΙΖΑ ΑΛΕΞΙΑΔΟΥ', 'ΒΕΖΑΣΗΣ ΕΥΘΥΜΙΟΣ', 'ΕΛΛΗ ΑΓΓΕΛΑΚΟΠΟΥΛΟΥ', 'ΔΕΣΠΟΙΝΑ ΧΑΤΖΗΔΡΟΣΟΥ', 'ΒΑΣΙΛΙΚΗ ΛΑΖΟΥ', 'ΑΝΔΡΙΑΝΑ ΔΕΛΕΓΚΟΥ', 'ΑΠΟΣΤΟΛΙΑ ΠΛΙΑΣΣΑ', 'ΑΝΑΣΤΑΣΙΑ ΧΑΤΖΗΓΕΩΡΓΙΟΥ', 'ΑΛΙΚΗ ΒΑΒΟΥΓΥΙΟΥ ', 'ΜΕΛΙΝΑ ΑΛΕΞΙΑΔΟΥ', 'ΤΣΑΡΟΥΧΑΣ ΝΕΚΤΑΡΙΟΣ', 'ΜΠΟΤΣΩΛΗ ΑΙΚΑΤΕΡΙΝΗ', 'Ιωάννα Μιχαλοπούλου', 'Κατερίνα Μεργιάννη', 'ΕΛΕΝΗ ΜΑΡΓΑΡΙΤΗ', 'ΙΩΑΝΝΑ ΡΕΙΖΟΠΟΥΛΟΥ', 'ΝΙΚΟΛΑΟΣ ΠΑΠΑΓΓΕΛΟΠΟΥΛΟΣ', 'ΠΗΝΕΛΟΠΗ ΚΑΡΑΣΙΜΟΥ', 'Ελευθερία Κουμπουρλή', 'ΘΩΜΑΗ ΣΙΣΚΟΥ', 'Αλεξάνδρα Μωράτη', 'Χρυσούλα Παλαιολόγου', 'Κλεοπάτρα Χύτα', 'Χρυσαφένια Δεμέτη', 'ΣΥΜΕΛΑ ΤΣΑΟΥΣΟΓΛΟΥ', 'Δέσποινα Μαρία Σέργη', 'Αλέξανδρος Τάτσης', 'ΙΩΑΝΝΑ ΚΩΝΣΤΑΝΤΙΝΙΔΟΥ', 'Δήμητρα Χανδόλια', 'ΠΑΝΑΓΙΩΤΑ ΜΠΟΖΩΝΗ', 'ΟΥΡΑΝΙΑ ΦΑΝΟΥΡΑΚΗ', 'Σταυρούλα Λιβιτσάνου', 'ΑΓΛΑΪΑ ΝΙΚΟΛΟΠΟΥΛΟΥ', 'Στεργιανή Κατσιόλα', 'ΦΩΤΕΙΝΗ ΜΗΛΙΑΡΗ', 'ΑΡΤΕΜΙΣ ΜΑΚΡΗ', 'Γεώργιος Θεμελίδης', 'Πετρούλα Λιάκου', 'ΣΤΥΛΙΑΝΗ ΦΑΡΜΑΚΗ', 'Ελlένη Κοκκίου', 'ΝΑΛΜΠΑΝΤΗ ΔΗΜΗΤΡΑ', 'Ελένη Τσώτσου', 'Θεονύμφη Μπουχαλάκη', 'ΕΥΦΗΜΙΑ ΟΙΚΟΝΟΜΙΔΟΥ', 'Όλγα Σουρβίνου', 'ΔΗΜΗΤΡΙΟΣ ΠΑΝΤΕΛΑΚΗΣ', 'Ρεϊχάν Κιοσέ', 'ΤΕΡΕΖΑ ΙΩΑΝΝΑ ΨΥΛΛΑΚΗ', 'Άννα Σαμίου', 'Αντιγόνη Μούντζελου', 'ΘΕΟΔΩΡΑ ΜΑΡΙΝΑΤΟΥ', 'ΑΛΕΞΑΝΔΡΑ ΠΑΠΑΔΗΜΗΤΡΙΟΥ', 'Χρυσούλα Σκλαβενίτη', 'ΒΑΪΑ ΠΑΠΑΓΕΩΡΓΙΟΥ', 'Κατερίνα Κοντακτσή', 'Χριστίνα Τάτση', 'ΠΑΣΧΑΛΙΤΣΑ ΔΟΚΟΠΟΥΛΟΥ', 'Καλιτσουνάκη Κατερίνα', 'Άννα Μπαξεβάνη', 'ΕΙΡΗΝΗ-ΣΤΕΡΓΙΑΝΗ ΚΟΥΝΤΟΥΡΑ', 'Ευδοκία Φιδανάκη', 'ΣΟΦΙΑ ΔΙΤΣΟΥΔΗ', 'ΑΝΝΑ ΚΙΡΚΟΥΔΗ', 'Κλεονίκη Κατωγιάννη', 'Σημέλα Παπαδοπούλου', 'Ειρήνη Γραφάκου', 'ΒΑΓΙΑ ΜΑΝΤΕΛΑ', 'ΒΑΣΙΛΙΚΗ ΜΙΧΑΛΟΠΟΥΛΟΥ', 'Κυριακή Φωτιάδου', 'Αναστασία Μαυρίδου', 'Μαρία Καλεμκερίδου', 'ΝΙΚΟΛΙΑ ΤΣΙΑΚΟΥ', 'Γεώργιος Μπαντής', 'ΑΝΑΣΤΑΣΙΑ ΜΠΟΥΛΟΥΚΗ', 'ΜΑΡΙΝΑ ΛΑΜΠΑΚΗ', 'Ζωή Χύτα', 'ΧΡΙΣΤΙΝΑ ΠΑΛΑΙΟΛΟΓΟΥ', 'ΘΕΟΔΟΡΑ ΣΙΣΜΑΝΙΔΟΥ', 'ΤΡΙΑΝΤΑΦΥΛΛΙΑ ΔΙΑΜΑΝΤΗ', 'ΓΕΩΡΓΙΑ ΤΣΑΜΗ', 'Πηγή Μπάρμπα', 'ΦΩΤΙΟΣ ΠΑΝΑΓΙΩΤΟΠΟΥΛΟΣ', 'Ευαγγελία Παπαδοπούλου', 'ΑΛΕΞΑΝΔΡΑ ΚΑΡΑΚΩΣΤΑ', 'Βαλεντίνη Αντωνία Τσιροπούλου', 'ΠΕΤΡΟΒΑ ΠΑΡΑΣΚΕΥΗ', 'ΔΗΜΗΤΡΑ ΘΕΟΔΩΡΑΚΟΠΟΥΛΟΥ', 'Ειρήνη Δολαψάκη', 'ΚΩΝΣΤΑΝΤΙΝΙΑ ΝΤΟΝΤΗ', 'Μαρία Καρχαριδου', 'Ζωή Μουλαρά', 'Γαρυφαλιά Χαϊδοπούλου', 'ΔΗΜΗΤΡΑ ΚΑΛΟΓΡΑΙΑΚΗ', 'ΕΙΡΗΝΗ ΠΑΝΑΓΙΩΤΟΥ', 'ΜΑΡΙΑ ΧΑΛΑΡΗ', 'ΠΑΡΑΣΚΕΥΑΣ ΚΟΥΚΟΣ', 'Βασιλική Παπά', 'ΑΙΚΑΤΕΡΙΝΗ ΚΑΤΣΟΥΓΙΑΝΝΗ', 'ΔΗΜΗΤΡΑ ΔΟΥΖΔΑΜΠΑΝΗ', 'ΑΝΝΑ ΤΖΩΡΤΖΑΤΟΥ', 'Θεοδωρα Λιάγκα', 'Ελένη Μπούζτου', 'ΚΑΛΛΙΟΠΗ ΜΠΟΧΤΗ', 'Δέσποινα Σούρλα', 'ΔΙΜΗΤΡΑ ΜΑΚΑΡΟΝΗ', 'Δήμητρα Παλέγκα', 'ΔΕΣΠΟΙΝΑ ΠΑΡΑΣΤΑΤΙΔΟΥ', 'ΙΩΑΝΝΑ ΖΩΗ ΡΟΥΣΣΟΥ', 'Ειρήνη Ζούμπου', 'ΑΝΑΣΤΑΣΙΑ ΚΙΚΙΛΙΓΚΑ', 'ΕΛΠΙΣ ΣΟΥΙΚΛΙΩΤΗ', 'ΣΤΥΛΙΑΝΗ ΚΟΥΜΠΕΝΑΚΗ', 'Κυριακή Πασχαλίδου', 'ΠΑΡΑΣΚΕΥΗ ΚΑΡΑΝΙΚΟΛΑ', 'Μαρία Πλιόγκα', 'Θεοδώρα Σισμανίδου', 'ΚΡΥΣΤΑΛΛΙΑ ΚΟΥΙΔΟΥ', 'ΔΗΜΗΤΡΗΣ ΣΑΒΒΑΚΗΣ', 'ΠΑΝΑΓΙΩΤΑ ΠΑΠΑΔΟΠΟΥΛΟΥ', 'Σοφία Τσιράκη', 'Κωνσταντια Δραγκα', 'ΜΑΡΙΑ ΚΙΑΓΙΑ', 'Ελένη Ευτυχία Κωστίδη']
# usernames=['labrianatsiak@icloud.com', 'nikosmariagr@hotmail.com', 'kampel85@yahoo.gr', 'spaeirhnh@hotmail.com', 'tatianapsychology@yahoo.gr', 'eugenia.tragaki@gmail.com', 'nsvalv@gmail.com', 'sofiagidari@yahoo.gr', 'darv009@hotmail.com', 'vgiota83@hotmail.com', 'emmavasi76@gmail.com', 'maria.gr.bl@hotmail.com', 'elpidagoukou@yahoo.gr', 'terzoydi@gmail.com', 'tzovel72@yahoo.gr', 'maria-terzi@hotmail.com', 'mgeorgopoulou@gmail.com', 'vandrout@yahoo.gr', 'christina.albani@yahoo.gr', 'theodoragouna@gmail.com', 'magathou@hotmail.com', 'alexiosarfanis@gmail.com', 'lillyvarsama@yahoo.com', 'voulgaridou.christina@gmail.com', 'depi1970@hotmail.com', 'kgkagkali@gmail.com', 'alexandralt@yahoo.com', 'louiza.alex@gmail.com', 'efthymis.v@gmail.com', 'elliaggel@gmail.com', 'deppy.h@hotmail.com', 'lazouvaso@yahoo.gr', 'delegouandriana@yahoo.gr', 'litsapliassa@gmail.com', 'anastasiachatz3012@gmail.com', 'alikakiv_1986@hotmail.com', 'melinalexiadou@gmail.com', 'nectsarou@yahoo.gr', 'botsoli@yahoo.gr', 'joannamixalo@yahoo.gr', 'katmer2207@gmail.com', 'elenaki_m@yahoo.gr', 'reizjoanna@gmail.com', 'drnjp@hotmail.com', 'pinelopimesag@gmail.com', 'ekoumpourli@gmail.com', 'thomiesis@gmail.com', 'antamorati@gmail.com', 'chrisoula_pal@hotmail.com', 'kleopatra202008@hotmail.com', 'xryfede@hotmail.com', 'tsaousamel@hotmail.com', 'debbiemariasergi@gmail.com', 'alextts84@gmail.com', 'gianna_konsta1@yahoo.gr', 'dimitisdimitra@gmail.com', 'panagiwtamp@gmail.com', 'raniafanour@hotmail.com', 'loriliv@hotmail.com', 'lia.nikolomi@gmail.com', 'stergianikats@yahoo.com', 'feniamili@hotmail.com', 'stylianosmakris@gmail.com', 'giorgos.themelidis@gmail.com', 'lpenny20111@gmail.com', 'stellariafarmaki@gmail.com', 'elenikok756@gmail.com', 'naldimitra1974@gmail.com', 'elenits2001@gmail.com', 'theonhmp@gmail.com', 'efioikonomidou@gmail.com', 'olgasourv121993@yahoo.gr', 'sioteiri@hotmail.gr', 'reyhankiose@windowslive.com', 'tpsyllaki@gmail.com', 'samanna82@gmail.com', 'antigonimountzelou@gmail.com', 'dmarinatou@gmail.com', 'alexpap070399@gmail.com', 'crissperly@gmail.com', 'papageorgiou_vaia@yahoo.gr', 'katkonta@gmail.com', 'achristinatatsi@gmail.com', 'linadokopou@yahoo.gr', 'kkalitsounaki@gmail.com', 'annabaxe87@gmail.com', 'eirinikoun@gmail.com', 'fidanaki123@gmail.com', 'sofi53@windowslive.com', 'anna.kirkoudi@gmail.com', 'niki.katogianni@gmail.com', 'simelapap@gmail.com', 'egrafakou@gmail.com', 'csioannina@yahoo.gr', 'vamix2007@yahoo.gr', 'kikifotiad@gmail.com', 'anastmavr@gmail.com', 'mia123kal4@gmail.com', 'nikitsiakou@gmail.com', 'bantisg1@otenet.gr', 'anboulouki@gmail.com', 'marinae_mail@yahoo.gr', 'zoichyta@gmail.com', 'buzantio@hotmail.com', 'theodora_sismanidou@hotmail.com', 'rose.diamanti@gmail.com', 'gt88_@hotmail.com', 'pigibarmpa@hotmail.com', 'panagiotoglou2@gmail.com', 'epapadop13@gmail.com', 'alexandrakarakosta.ak@gmail.com', 'tsiropoulou.valentini@gmail.com', 'vivaki_1993@yahoo.gr', 'theodorakopoulou.psy@gmail.com', 'eirhnhdol@gmail.com', 'kntonti2014@gmail.com', 'karxaridoumaria27@gmail.com', 'zoemoulara@gmail.com', 'litsa.xaidopoulou@gmail.com', 'didaorestiada@gmail.com', 'eirpan2203@yahoo.com', 'mariachalari83@gmail.com', 'parikouko@gmail.com', 'vasiapapa@gmail.com', 'katsougiannik@gmail.com', 'dimitradouzdampani@gmail.com', 'tzortzatou@gmail.com', 'theodoraliaga2003@gmal.com', 'bouztoue@gmail.com', 'kelly.bochti@yahoo.com', 'dsourla@yahoo.gr', 'dimitramakslt@gmail.com', 'dimitra.pal1@hotmail.com', 'tetaparastatidou@yahoo.gr', 'gz.roussou@hotmail.com', 'eirinizoumpou@yahoo.gr', 'anastasia.x.kikiligka@gmail.com', 'elpsou@gmail.com', 'stkoubenaki@yahoo.gr', 'dpashalidou@yahoo.gr', 'panagiotiskitis@yahoo.gr', 'mariaplioga@gmail.com', 'theodora.sismanidou9@gmail.com', 'krystalk.dask@yahoo.gr', 'savvakisd@gmail.com', 'papadopa3@gmail.com', 'sofiats87@gmail.com', 'dragakonstantia@gmail.com', 'marouli1980@yahoo.gr', 'ekostide@gmail.com']
# passwords=['kKw63vspMq', 'AV2wPELFZS', 'BK259LtGwu', 'a6BzbdXRJu', 'mLTcrCs6a9', 'Jv37HCYAMX', 'j8m7Dn4VHQ', 'AXJLQHhw7d', 'ZUc9n2gWVp', 'Hvuk4aspx7', 'MLVTdK26SB', 'UpZcq6hKTC', 'paT7jEgSAw', 'eH6ZDwbk2N', 'Wzp96ykNeD', 'tSYcA8GPCJ', 'w3XjgRETsL', 'Hy26wLYmzk', 'GsBEYywW9n', 'TpSe6atkf2', 'pJH9CA7L2g', 'L4UWEuD8MA', 'Q2GTuYE8ch', 'xcA43GJWaf', 'u46UXerHf9', 'Nz58pmgUDF', 'prF4k9VXb2', 'E8L4MjXsWe', 'UxYV7bNfv4', 'Aax5Xe3pTK', 'RTFtj7Vg3x', 'X94bWctMj5', 'TEahK53skD', 'YFDHf4cB8n', 'jPsvBFte7z', 'ZuAf4sPJUw', 'wWgcxYk7M2', 'M5Dr8aJxhy', 'zPeaCyw3nq', 'xK6fdCh957', 'FmLV3yETru', 'Luh5DAsG3z', 'C9LAyaVnG4', 'QgK64HvXbs', 'vk3d548UTh', 'j3yW5wTMmX', 'Kaj7SLhUgb', 's7nCSxg8D6', 'Ud3aV4KxDv', 'gWEu5mP9af', 'KEg9Lf5acb', 'mJ7S4fRDKG', 'VLnz95ATF3', 'YjRHyW2kU3', 'YrSkWj8wXp', 'f2qecKdsgR', 'zLch3KQ4Yg', 'S4Gn9NEpjz', 'r36bCMyk2K', 'CRnKGw3Lmx', 'gECXFsJ2zV', 'RxHtjBkG4g', 'meCVcW3jGp', 'DXMWE6sgGn', 'TMvU6FnpPx', 'gj7KYfCXLc', 'sj382GLBMS', 'tv8q5TmKzF', 'K8scC4kJ3v', 'vy2BsQg6Wz', 'mRDFz8W43b', 'Ffr8nHcKYp', 'DsS32w85u7', 'ntUAeEV3WD', 'z8vGFDBMAQ', 'L6cZWVmsu8', 'SJ6pHmh7Ck', 'C8fexZT4R6', 'Hkw4mA3ZLF', 's8FEaD4cnB', 'u8amQwTbSX', 'mfwYVs6F2C', 'cz24J8fEKh', 'q3PSAeUnba', 'fA32gRKkXs', 'zcT5ZD6GsU', 'ZYf6e8tSXp', 'adWLg2ZUAV', 'vqwZS97Td2', 'AfTM7s9NpF', 'CpN8BKV2g4', 'nBzEkMy2jR', 'T3HK8f2wJg', 't7wezY2kPd', 'AKbn43mHY8', 'a7Z8duAUpD', 'bu9SEjGyfY', 'jv6Ek4rTgy', 'mMDd5Ra48f', 'UKqQjgaT9x', 'GESLcDg7jv', 'UDMgpm8zJR', 'x6tsTVapr5', 'u3ajr4kARH', 'QZe4xc2ATW', 'FdC95n2ZVw', 'G3VfyYQk9a', 'TEQ4xHvCt9', 'Mt9YH4jqeb', 'AP3xcv2VhX', 'XqpwB9Yv36', 'D85kt7GqfB', 'gpvK2b93Hq', 'zmwjbV3PTs', 'JTwkqVm2Kv', 'fq3cQWnjLR', 'zp35YamjRk', 'bwTXtGj4AZ', 'FC5vzgNrEL', 'KJE3PHhysB', 'A9xQmcH8jJ', 'j2K3hyV76L', 'bu5dhCHMcm', 'wmzHq8pWJG', 'EfTp8J5Duc', 'bTD58pkXCM', 'FZ5JYXnrMW', 'Q6537xmUrC', 'L2SkFNRn63', 'b6Yds7VLqk', 'bDUqJS4gLs', 'PJeuq3KH5p', 'hayN4S5KXV', 'c9uPY7fKbt', 'L6TbYtG274', 'WEVHfGnt2v', 'CXbg9QFMaw', 'Wz2YvXraCx', 'dVLJx5qRjS', 'sT3Q8PEVBx', 'dN5xw4h7Vq', 'dhpmqKQX9G', 'Ye69CpUFxq', 'Sd69btzrYy', 'g2PjzQxk9y', 'BMQ8fz2dc3', 'f4JHZBprSG', 'UrYqaAP3RM', 'yaXBdn6ATM', 'HqyK874k2g']
# periods=['11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '11-19 Μαρτίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου', '2- 16 Απριλίου']

data=[
    {
        "name": "ΛΑΜΠΡΙΑΝΑ ΤΣΙΑΚΠΙΝΗ",
        "email": "labrianatsiak@icloud.com",
        "password": "kKw63vspMq",
        "period": "11-19 Μαρτίου"
    },
    {
        "name": "ΜΑΡΙΑ - ΕΙΡΗΝΗ ΓΑΛΕΡΑΚΗ",
        "email": "nikosmariagr@hotmail.com",
        "password": "AV2wPELFZS",
        "period": "11-19 Μαρτίου"
    },
    {
        "name": "ΚΟΥΛΑ ΑΜΠΕΛΙΟΤΗ",
        "email": "kampel85@yahoo.gr",
        "password": "BK259LtGwu",
        "period": "11-19 Μαρτίου"
    },
    {
        "name": "ΕΙΡΗΝΗ ΑΝΑΤΣΟΥΤΣΟΥΛΑ",
        "email": "spaeirhnh@hotmail.com",
        "password": "a6BzbdXRJu",
        "period": "11-19 Μαρτίου"
    },
    {
        "name": "ΤΑΤΙΑΝΑ ΕΛΕΟΝΩΡΑ ΑΝΑΓΝΩΣΤΙΔΟΥ",
        "email": "tatianapsychology@yahoo.gr",
        "password": "mLTcrCs6a9",
        "period": "11-19 Μαρτίου"
    },
    {
        "name": "ΕΥΓΕΝΙΑ ΤΡΑΓΑΚΗ",
        "email": "eugenia.tragaki@gmail.com",
        "password": "Jv37HCYAMX",
        "period": "11-19 Μαρτίου"
    },
    {
        "name": "ΣΠΥΡΙΔΩΝ ΒΑΛΒΗΣ",
        "email": "nsvalv@gmail.com",
        "password": "j8m7Dn4VHQ",
        "period": "11-19 Μαρτίου"
    },
    {
        "name": "ΣΟΦΙΑ ΓΙΔΑΡΗ",
        "email": "sofiagidari@yahoo.gr",
        "password": "AXJLQHhw7d",
        "period": "11-19 Μαρτίου"
    },
    {
        "name": "ΔΗΜΗΤΡΗΣ ΑΡΒΑΝΙΤΗΣ",
        "email": "darv009@hotmail.com",
        "password": "ZUc9n2gWVp",
        "period": "11-19 Μαρτίου"
    },
    {
        "name": "ΠΑΝΑΓΙΩΤΑ ΒΑΣΙΛΕΙΟΥ",
        "email": "vgiota83@hotmail.com",
        "password": "Hvuk4aspx7",
        "period": "11-19 Μαρτίου"
    },
    {
        "name": "ΕΜΜΑΝΟΥΕΛΑ ΒΑΣΙΛΕΙΑΔΗ",
        "email": "emmavasi76@gmail.com",
        "password": "MLVTdK26SB",
        "period": "11-19 Μαρτίου"
    },
    {
        "name": "ΜΑΡΙΑ ΓΟΥΡΓΙΩΤΗ",
        "email": "maria.gr.bl@hotmail.com",
        "password": "UpZcq6hKTC",
        "period": "11-19 Μαρτίου"
    },
    {
        "name": "ΕΛΠΙΔΑ ΓΟΥΚΟΥ",
        "email": "elpidagoukou@yahoo.gr",
        "password": "paT7jEgSAw",
        "period": "11-19 Μαρτίου"
    },
    {
        "name": "ΜΑΡΙΑ ΤΕΡΖΟΥΔΗ",
        "email": "terzoydi@gmail.com",
        "password": "eH6ZDwbk2N",
        "period": "11-19 Μαρτίου"
    },
    {
        "name": "ΓΕΩΡΓΙΑ ΒΕΛΟΥΔΟΥ",
        "email": "tzovel72@yahoo.gr",
        "password": "Wzp96ykNeD",
        "period": "11-19 Μαρτίου"
    },
    {
        "name": "ΜΑΡΙΑ ΤΕΡΖΗ",
        "email": "maria-terzi@hotmail.com",
        "password": "tSYcA8GPCJ",
        "period": "11-19 Μαρτίου"
    },
    {
        "name": "ΜΑΡΙΑ ΓΕΩΡΓΟΠΟΥΛΟΥ",
        "email": "mgeorgopoulou@gmail.com",
        "password": "w3XjgRETsL",
        "period": "11-19 Μαρτίου"
    },
    {
        "name": "ΒΑΣΣΟ ΑΝΔΡΟΥΤΣΟΥ",
        "email": "vandrout@yahoo.gr",
        "password": "Hy26wLYmzk",
        "period": "11-19 Μαρτίου"
    },
    {
        "name": "ΧΡΗΣΤΙΝΑ ΑΛΒΑΝΗ",
        "email": "christina.albani@yahoo.gr",
        "password": "GsBEYywW9n",
        "period": "11-19 Μαρτίου"
    },
    {
        "name": "ΘΕΟΔΩΡΑ ΓΚΟΥΝΑ",
        "email": "theodoragouna@gmail.com",
        "password": "TpSe6atkf2",
        "period": "11-19 Μαρτίου"
    },
    {
        "name": "ΜΑΡΙΑ ΑΓΑΘΟΥ",
        "email": "magathou@hotmail.com",
        "password": "pJH9CA7L2g",
        "period": "11-19 Μαρτίου"
    },
    {
        "name": "ΑΛΕΞΙΟΣ ΑΡΦΑΝΗΣ",
        "email": "alexiosarfanis@gmail.com",
        "password": "L4UWEuD8MA",
        "period": "11-19 Μαρτίου"
    },
    {
        "name": "ΕΥΑΓΓΕΛΙΑ ΒΑΡΣΑΜΑ",
        "email": "lillyvarsama@yahoo.com",
        "password": "Q2GTuYE8ch",
        "period": "11-19 Μαρτίου"
    },
    {
        "name": "ΧΡΗΣΤΙΝΑ ΒΟΥΛΓΑΡΙΔΟΥ",
        "email": "voulgaridou.christina@gmail.com",
        "password": "xcA43GJWaf",
        "period": "11-19 Μαρτίου"
    },
    {
        "name": "ΔΕΣΠΟΙΝΑ ΑΒΡΑΜΙΔΟΥ",
        "email": "depi1970@hotmail.com",
        "password": "u46UXerHf9",
        "period": "11-19 Μαρτίου"
    },
    {
        "name": "ΑΙΚΑΤΕΡΙΝΗ ΓΚΑΓΚΑΛΗ",
        "email": "kgkagkali@gmail.com",
        "password": "Nz58pmgUDF",
        "period": "11-19 Μαρτίου"
    },
    {
        "name": "ΑΛΕΞΑΝΔΡΑ ΑΛΤΙΠΑΡΜΑΚΗ",
        "email": "alexandralt@yahoo.com",
        "password": "prF4k9VXb2",
        "period": "11-19 Μαρτίου"
    },
    {
        "name": "ΛΟΥΙΖΑ ΑΛΕΞΙΑΔΟΥ",
        "email": "louiza.alex@gmail.com",
        "password": "E8L4MjXsWe",
        "period": "11-19 Μαρτίου"
    },
    {
        "name": "ΒΕΖΑΣΗΣ ΕΥΘΥΜΙΟΣ",
        "email": "efthymis.v@gmail.com",
        "password": "UxYV7bNfv4",
        "period": "11-19 Μαρτίου"
    },
    {
        "name": "ΕΛΛΗ ΑΓΓΕΛΑΚΟΠΟΥΛΟΥ",
        "email": "elliaggel@gmail.com",
        "password": "Aax5Xe3pTK",
        "period": "11-19 Μαρτίου"
    },
    {
        "name": "ΔΕΣΠΟΙΝΑ ΧΑΤΖΗΔΡΟΣΟΥ",
        "email": "deppy.h@hotmail.com",
        "password": "RTFtj7Vg3x",
        "period": "11-19 Μαρτίου"
    },
    {
        "name": "ΒΑΣΙΛΙΚΗ ΛΑΖΟΥ",
        "email": "lazouvaso@yahoo.gr",
        "password": "X94bWctMj5",
        "period": "11-19 Μαρτίου"
    },
    {
        "name": "ΑΝΔΡΙΑΝΑ ΔΕΛΕΓΚΟΥ",
        "email": "delegouandriana@yahoo.gr",
        "password": "TEahK53skD",
        "period": "11-19 Μαρτίου"
    },
    {
        "name": "ΑΠΟΣΤΟΛΙΑ ΠΛΙΑΣΣΑ",
        "email": "litsapliassa@gmail.com",
        "password": "YFDHf4cB8n",
        "period": "11-19 Μαρτίου"
    },
    {
        "name": "ΑΝΑΣΤΑΣΙΑ ΧΑΤΖΗΓΕΩΡΓΙΟΥ",
        "email": "anastasiachatz3012@gmail.com",
        "password": "jPsvBFte7z",
        "period": "11-19 Μαρτίου"
    },
    {
        "name": "ΑΛΙΚΗ ΒΑΒΟΥΓΥΙΟΥ ",
        "email": "alikakiv_1986@hotmail.com",
        "password": "ZuAf4sPJUw",
        "period": "11-19 Μαρτίου"
    },
    {
        "name": "ΜΕΛΙΝΑ ΑΛΕΞΙΑΔΟΥ",
        "email": "melinalexiadou@gmail.com",
        "password": "wWgcxYk7M2",
        "period": "11-19 Μαρτίου"
    },
    {
        "name": "ΤΣΑΡΟΥΧΑΣ ΝΕΚΤΑΡΙΟΣ",
        "email": "nectsarou@yahoo.gr",
        "password": "M5Dr8aJxhy",
        "period": "11-19 Μαρτίου"
    },
    {
        "name": "ΜΠΟΤΣΩΛΗ ΑΙΚΑΤΕΡΙΝΗ",
        "email": "botsoli@yahoo.gr",
        "password": "zPeaCyw3nq",
        "period": "11-19 Μαρτίου"
    },
    {
        "name": "Ιωάννα Μιχαλοπούλου",
        "email": "joannamixalo@yahoo.gr",
        "password": "xK6fdCh957",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "Κατερίνα Μεργιάννη",
        "email": "katmer2207@gmail.com",
        "password": "FmLV3yETru",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "ΕΛΕΝΗ ΜΑΡΓΑΡΙΤΗ",
        "email": "elenaki_m@yahoo.gr",
        "password": "Luh5DAsG3z",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "ΙΩΑΝΝΑ ΡΕΙΖΟΠΟΥΛΟΥ",
        "email": "reizjoanna@gmail.com",
        "password": "C9LAyaVnG4",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "ΝΙΚΟΛΑΟΣ ΠΑΠΑΓΓΕΛΟΠΟΥΛΟΣ",
        "email": "drnjp@hotmail.com",
        "password": "QgK64HvXbs",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "ΠΗΝΕΛΟΠΗ ΚΑΡΑΣΙΜΟΥ",
        "email": "pinelopimesag@gmail.com",
        "password": "vk3d548UTh",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "Ελευθερία Κουμπουρλή",
        "email": "ekoumpourli@gmail.com",
        "password": "j3yW5wTMmX",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "ΘΩΜΑΗ ΣΙΣΚΟΥ",
        "email": "thomiesis@gmail.com",
        "password": "Kaj7SLhUgb",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "Αλεξάνδρα Μωράτη",
        "email": "antamorati@gmail.com",
        "password": "s7nCSxg8D6",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "Χρυσούλα Παλαιολόγου",
        "email": "chrisoula_pal@hotmail.com",
        "password": "Ud3aV4KxDv",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "Κλεοπάτρα Χύτα",
        "email": "kleopatra202008@hotmail.com",
        "password": "gWEu5mP9af",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "Χρυσαφένια Δεμέτη",
        "email": "xryfede@hotmail.com",
        "password": "KEg9Lf5acb",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "ΣΥΜΕΛΑ ΤΣΑΟΥΣΟΓΛΟΥ",
        "email": "tsaousamel@hotmail.com",
        "password": "mJ7S4fRDKG",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "Δέσποινα Μαρία Σέργη",
        "email": "debbiemariasergi@gmail.com",
        "password": "VLnz95ATF3",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "Αλέξανδρος Τάτσης",
        "email": "alextts84@gmail.com",
        "password": "YjRHyW2kU3",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "ΙΩΑΝΝΑ ΚΩΝΣΤΑΝΤΙΝΙΔΟΥ",
        "email": "gianna_konsta1@yahoo.gr",
        "password": "YrSkWj8wXp",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "Δήμητρα Χανδόλια",
        "email": "dimitisdimitra@gmail.com",
        "password": "f2qecKdsgR",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "ΠΑΝΑΓΙΩΤΑ ΜΠΟΖΩΝΗ",
        "email": "panagiwtamp@gmail.com",
        "password": "zLch3KQ4Yg",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "ΟΥΡΑΝΙΑ ΦΑΝΟΥΡΑΚΗ",
        "email": "raniafanour@hotmail.com",
        "password": "S4Gn9NEpjz",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "Σταυρούλα Λιβιτσάνου",
        "email": "loriliv@hotmail.com",
        "password": "r36bCMyk2K",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "ΑΓΛΑΪΑ ΝΙΚΟΛΟΠΟΥΛΟΥ",
        "email": "lia.nikolomi@gmail.com",
        "password": "CRnKGw3Lmx",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "Στεργιανή Κατσιόλα",
        "email": "stergianikats@yahoo.com",
        "password": "gECXFsJ2zV",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "ΦΩΤΕΙΝΗ ΜΗΛΙΑΡΗ",
        "email": "feniamili@hotmail.com",
        "password": "RxHtjBkG4g",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "ΑΡΤΕΜΙΣ ΜΑΚΡΗ",
        "email": "stylianosmakris@gmail.com",
        "password": "meCVcW3jGp",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "Γεώργιος Θεμελίδης",
        "email": "giorgos.themelidis@gmail.com",
        "password": "DXMWE6sgGn",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "Πετρούλα Λιάκου",
        "email": "lpenny20111@gmail.com",
        "password": "TMvU6FnpPx",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "ΣΤΥΛΙΑΝΗ ΦΑΡΜΑΚΗ",
        "email": "stellariafarmaki@gmail.com",
        "password": "gj7KYfCXLc",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "Ελlένη Κοκκίου",
        "email": "elenikok756@gmail.com",
        "password": "sj382GLBMS",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "ΝΑΛΜΠΑΝΤΗ ΔΗΜΗΤΡΑ",
        "email": "naldimitra1974@gmail.com",
        "password": "tv8q5TmKzF",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "Ελένη Τσώτσου",
        "email": "elenits2001@gmail.com",
        "password": "K8scC4kJ3v",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "Θεονύμφη Μπουχαλάκη",
        "email": "theonhmp@gmail.com",
        "password": "vy2BsQg6Wz",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "ΕΥΦΗΜΙΑ ΟΙΚΟΝΟΜΙΔΟΥ",
        "email": "efioikonomidou@gmail.com",
        "password": "mRDFz8W43b",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "Όλγα Σουρβίνου",
        "email": "olgasourv121993@yahoo.gr",
        "password": "Ffr8nHcKYp",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "ΔΗΜΗΤΡΙΟΣ ΠΑΝΤΕΛΑΚΗΣ",
        "email": "sioteiri@hotmail.gr",
        "password": "DsS32w85u7",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "Ρεϊχάν Κιοσέ",
        "email": "reyhankiose@windowslive.com",
        "password": "ntUAeEV3WD",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "ΤΕΡΕΖΑ ΙΩΑΝΝΑ ΨΥΛΛΑΚΗ",
        "email": "tpsyllaki@gmail.com",
        "password": "z8vGFDBMAQ",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "Άννα Σαμίου",
        "email": "samanna82@gmail.com",
        "password": "L6cZWVmsu8",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "Αντιγόνη Μούντζελου",
        "email": "antigonimountzelou@gmail.com",
        "password": "SJ6pHmh7Ck",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "ΘΕΟΔΩΡΑ ΜΑΡΙΝΑΤΟΥ",
        "email": "dmarinatou@gmail.com",
        "password": "C8fexZT4R6",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "ΑΛΕΞΑΝΔΡΑ ΠΑΠΑΔΗΜΗΤΡΙΟΥ",
        "email": "alexpap070399@gmail.com",
        "password": "Hkw4mA3ZLF",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "Χρυσούλα Σκλαβενίτη",
        "email": "crissperly@gmail.com",
        "password": "s8FEaD4cnB",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "ΒΑΪΑ ΠΑΠΑΓΕΩΡΓΙΟΥ",
        "email": "papageorgiou_vaia@yahoo.gr",
        "password": "u8amQwTbSX",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "Κατερίνα Κοντακτσή",
        "email": "katkonta@gmail.com",
        "password": "mfwYVs6F2C",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "Χριστίνα Τάτση",
        "email": "achristinatatsi@gmail.com",
        "password": "cz24J8fEKh",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "ΠΑΣΧΑΛΙΤΣΑ ΔΟΚΟΠΟΥΛΟΥ",
        "email": "linadokopou@yahoo.gr",
        "password": "q3PSAeUnba",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "Καλιτσουνάκη Κατερίνα",
        "email": "kkalitsounaki@gmail.com",
        "password": "fA32gRKkXs",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "Άννα Μπαξεβάνη",
        "email": "annabaxe87@gmail.com",
        "password": "zcT5ZD6GsU",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "ΕΙΡΗΝΗ-ΣΤΕΡΓΙΑΝΗ ΚΟΥΝΤΟΥΡΑ",
        "email": "eirinikoun@gmail.com",
        "password": "ZYf6e8tSXp",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "Ευδοκία Φιδανάκη",
        "email": "fidanaki123@gmail.com",
        "password": "adWLg2ZUAV",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "ΣΟΦΙΑ ΔΙΤΣΟΥΔΗ",
        "email": "sofi53@windowslive.com",
        "password": "vqwZS97Td2",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "ΑΝΝΑ ΚΙΡΚΟΥΔΗ",
        "email": "anna.kirkoudi@gmail.com",
        "password": "AfTM7s9NpF",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "Κλεονίκη Κατωγιάννη",
        "email": "niki.katogianni@gmail.com",
        "password": "CpN8BKV2g4",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "Σημέλα Παπαδοπούλου",
        "email": "simelapap@gmail.com",
        "password": "nBzEkMy2jR",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "Ειρήνη Γραφάκου",
        "email": "egrafakou@gmail.com",
        "password": "T3HK8f2wJg",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "ΒΑΓΙΑ ΜΑΝΤΕΛΑ",
        "email": "csioannina@yahoo.gr",
        "password": "t7wezY2kPd",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "ΒΑΣΙΛΙΚΗ ΜΙΧΑΛΟΠΟΥΛΟΥ",
        "email": "vamix2007@yahoo.gr",
        "password": "AKbn43mHY8",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "Κυριακή Φωτιάδου",
        "email": "kikifotiad@gmail.com",
        "password": "a7Z8duAUpD",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "Αναστασία Μαυρίδου",
        "email": "anastmavr@gmail.com",
        "password": "bu9SEjGyfY",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "Μαρία Καλεμκερίδου",
        "email": "mia123kal4@gmail.com",
        "password": "jv6Ek4rTgy",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "ΝΙΚΟΛΙΑ ΤΣΙΑΚΟΥ",
        "email": "nikitsiakou@gmail.com",
        "password": "mMDd5Ra48f",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "Γεώργιος Μπαντής",
        "email": "bantisg1@otenet.gr",
        "password": "UKqQjgaT9x",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "ΑΝΑΣΤΑΣΙΑ ΜΠΟΥΛΟΥΚΗ",
        "email": "anboulouki@gmail.com",
        "password": "GESLcDg7jv",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "ΜΑΡΙΝΑ ΛΑΜΠΑΚΗ",
        "email": "marinae_mail@yahoo.gr",
        "password": "UDMgpm8zJR",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "Ζωή Χύτα",
        "email": "zoichyta@gmail.com",
        "password": "x6tsTVapr5",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "ΧΡΙΣΤΙΝΑ ΠΑΛΑΙΟΛΟΓΟΥ",
        "email": "buzantio@hotmail.com",
        "password": "u3ajr4kARH",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "ΘΕΟΔΟΡΑ ΣΙΣΜΑΝΙΔΟΥ",
        "email": "theodora_sismanidou@hotmail.com",
        "password": "QZe4xc2ATW",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "ΤΡΙΑΝΤΑΦΥΛΛΙΑ ΔΙΑΜΑΝΤΗ",
        "email": "rose.diamanti@gmail.com",
        "password": "FdC95n2ZVw",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "ΓΕΩΡΓΙΑ ΤΣΑΜΗ",
        "email": "gt88_@hotmail.com",
        "password": "G3VfyYQk9a",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "Πηγή Μπάρμπα",
        "email": "pigibarmpa@hotmail.com",
        "password": "TEQ4xHvCt9",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "ΦΩΤΙΟΣ ΠΑΝΑΓΙΩΤΟΠΟΥΛΟΣ",
        "email": "panagiotoglou2@gmail.com",
        "password": "Mt9YH4jqeb",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "Ευαγγελία Παπαδοπούλου",
        "email": "epapadop13@gmail.com",
        "password": "AP3xcv2VhX",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "ΑΛΕΞΑΝΔΡΑ ΚΑΡΑΚΩΣΤΑ",
        "email": "alexandrakarakosta.ak@gmail.com",
        "password": "XqpwB9Yv36",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "Βαλεντίνη Αντωνία Τσιροπούλου",
        "email": "tsiropoulou.valentini@gmail.com",
        "password": "D85kt7GqfB",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "ΠΕΤΡΟΒΑ ΠΑΡΑΣΚΕΥΗ",
        "email": "vivaki_1993@yahoo.gr",
        "password": "gpvK2b93Hq",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "ΔΗΜΗΤΡΑ ΘΕΟΔΩΡΑΚΟΠΟΥΛΟΥ",
        "email": "theodorakopoulou.psy@gmail.com",
        "password": "zmwjbV3PTs",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "Ειρήνη Δολαψάκη",
        "email": "eirhnhdol@gmail.com",
        "password": "JTwkqVm2Kv",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "ΚΩΝΣΤΑΝΤΙΝΙΑ ΝΤΟΝΤΗ",
        "email": "kntonti2014@gmail.com",
        "password": "fq3cQWnjLR",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "Μαρία Καρχαριδου",
        "email": "karxaridoumaria27@gmail.com",
        "password": "zp35YamjRk",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "Ζωή Μουλαρά",
        "email": "zoemoulara@gmail.com",
        "password": "bwTXtGj4AZ",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "Γαρυφαλιά Χαϊδοπούλου",
        "email": "litsa.xaidopoulou@gmail.com",
        "password": "FC5vzgNrEL",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "ΔΗΜΗΤΡΑ ΚΑΛΟΓΡΑΙΑΚΗ",
        "email": "didaorestiada@gmail.com",
        "password": "KJE3PHhysB",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "ΕΙΡΗΝΗ ΠΑΝΑΓΙΩΤΟΥ",
        "email": "eirpan2203@yahoo.com",
        "password": "A9xQmcH8jJ",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "ΜΑΡΙΑ ΧΑΛΑΡΗ",
        "email": "mariachalari83@gmail.com",
        "password": "j2K3hyV76L",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "ΠΑΡΑΣΚΕΥΑΣ ΚΟΥΚΟΣ",
        "email": "parikouko@gmail.com",
        "password": "bu5dhCHMcm",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "Βασιλική Παπά",
        "email": "vasiapapa@gmail.com",
        "password": "wmzHq8pWJG",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "ΑΙΚΑΤΕΡΙΝΗ ΚΑΤΣΟΥΓΙΑΝΝΗ",
        "email": "katsougiannik@gmail.com",
        "password": "EfTp8J5Duc",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "ΔΗΜΗΤΡΑ ΔΟΥΖΔΑΜΠΑΝΗ",
        "email": "dimitradouzdampani@gmail.com",
        "password": "bTD58pkXCM",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "ΑΝΝΑ ΤΖΩΡΤΖΑΤΟΥ",
        "email": "tzortzatou@gmail.com",
        "password": "FZ5JYXnrMW",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "Θεοδωρα Λιάγκα",
        "email": "theodoraliaga2003@gmal.com",
        "password": "Q6537xmUrC",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "Ελένη Μπούζτου",
        "email": "bouztoue@gmail.com",
        "password": "L2SkFNRn63",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "ΚΑΛΛΙΟΠΗ ΜΠΟΧΤΗ",
        "email": "kelly.bochti@yahoo.com",
        "password": "b6Yds7VLqk",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "Δέσποινα Σούρλα",
        "email": "dsourla@yahoo.gr",
        "password": "bDUqJS4gLs",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "ΔΙΜΗΤΡΑ ΜΑΚΑΡΟΝΗ",
        "email": "dimitramakslt@gmail.com",
        "password": "PJeuq3KH5p",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "Δήμητρα Παλέγκα",
        "email": "dimitra.pal1@hotmail.com",
        "password": "hayN4S5KXV",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "ΔΕΣΠΟΙΝΑ ΠΑΡΑΣΤΑΤΙΔΟΥ",
        "email": "tetaparastatidou@yahoo.gr",
        "password": "c9uPY7fKbt",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "ΙΩΑΝΝΑ ΖΩΗ ΡΟΥΣΣΟΥ",
        "email": "gz.roussou@hotmail.com",
        "password": "L6TbYtG274",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "Ειρήνη Ζούμπου",
        "email": "eirinizoumpou@yahoo.gr",
        "password": "WEVHfGnt2v",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "ΑΝΑΣΤΑΣΙΑ ΚΙΚΙΛΙΓΚΑ",
        "email": "anastasia.x.kikiligka@gmail.com",
        "password": "CXbg9QFMaw",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "ΕΛΠΙΣ ΣΟΥΙΚΛΙΩΤΗ",
        "email": "elpsou@gmail.com",
        "password": "Wz2YvXraCx",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "ΣΤΥΛΙΑΝΗ ΚΟΥΜΠΕΝΑΚΗ",
        "email": "stkoubenaki@yahoo.gr",
        "password": "dVLJx5qRjS",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "Κυριακή Πασχαλίδου",
        "email": "dpashalidou@yahoo.gr",
        "password": "sT3Q8PEVBx",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "ΠΑΡΑΣΚΕΥΗ ΚΑΡΑΝΙΚΟΛΑ",
        "email": "panagiotiskitis@yahoo.gr",
        "password": "dN5xw4h7Vq",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "Μαρία Πλιόγκα",
        "email": "mariaplioga@gmail.com",
        "password": "dhpmqKQX9G",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "Θεοδώρα Σισμανίδου",
        "email": "theodora.sismanidou9@gmail.com",
        "password": "Ye69CpUFxq",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "ΚΡΥΣΤΑΛΛΙΑ ΚΟΥΙΔΟΥ",
        "email": "krystalk.dask@yahoo.gr",
        "password": "Sd69btzrYy",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "ΔΗΜΗΤΡΗΣ ΣΑΒΒΑΚΗΣ",
        "email": "savvakisd@gmail.com",
        "password": "g2PjzQxk9y",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "ΠΑΝΑΓΙΩΤΑ ΠΑΠΑΔΟΠΟΥΛΟΥ",
        "email": "papadopa3@gmail.com",
        "password": "BMQ8fz2dc3",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "Σοφία Τσιράκη",
        "email": "sofiats87@gmail.com",
        "password": "f4JHZBprSG",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "Κωνσταντια Δραγκα",
        "email": "dragakonstantia@gmail.com",
        "password": "UrYqaAP3RM",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "ΜΑΡΙΑ ΚΙΑΓΙΑ",
        "email": "marouli1980@yahoo.gr",
        "password": "yaXBdn6ATM",
        "period": "2- 16 Απριλίου"
    },
    {
        "name": "Ελένη Ευτυχία Κωστίδη",
        "email": "ekostide@gmail.com",
        "password": "HqyK874k2g",
        "period": "2- 16 Απριλίου"
    }
]

names=list()
for i in range (len(data)):
    print(data[i]["name"])
    names.append(data[i]["name"])

usernames=list()
for i in range (len(data)):
    print(data[i]["email"])
    usernames.append(data[i]["email"])


passwords=list()
for i in range (len(data)):
    print(data[i]["password"])
    passwords.append(data[i]["password"])

periods=list()
for i in range (len(data)):
    print(data[i]["period"])
    periods.append(data[i]["period"])

hashed_passwords = stauth.hasher(passwords).generate()

authenticator = stauth.authenticate(names,usernames,hashed_passwords,'some_cookie_name','some_signature_key',cookie_expiry_days=30)


name, authentication_status = authenticator.login('Login','main')

if authentication_status:
        # newhtml="""
        #     <!DOCTYPE html>
        #     <header></header>
        #     <style>
        #        .css-1v3fvcr{background: rgb(34,193,195);
        #         background: radial-gradient(circle, rgba(34,193,195,1) 46%, rgba(229,229,184,1) 100%);
        #         }
        #         div.css-nlntq9.e16nr0p33 p{background-color:white;
        #         }
        #         .css-nlntq9.e16nr0p33{}
        #         .block-container.css-12oz5g7.egzxvld2{background-color:white;
        #             border:5px solid black;
        #             border-radius:15px;
        #             margin-top:67px;
        #         }

        #         .title{}
        #         .css-1cpxqw2.edgvbvh5{background-color:orange;
        #             color: white;
        #         }
            
        #     </style>
        #     <body> 
        #     </body
        # """

        html2="""
            <!DOCTYPE html>
            <header></header>
            <style>
               
            
            </style>
            <body> 
                <ul>
                    <li>Πατήστε στο κουμπί "δημιουργία πιστοποιητικού" για να δημιουργήσετε το πιστοποιητικό σας</li>
                    <li>Αφού δημιουργήσετε το πιστοποιητικό σας, πατήστε στο κουμπί "παραλαβή πιστοποιητικού" για να κατεβάσετε το πιστοποιητικό σας</li>
                </ul>
            </body
        """
        html3="""
            <!DOCTYPE html>
            <header></header>
 
            <body> 
               <h3 style="text-align:center;">🎓 Εκτυπώστε το πιστοποιητικό σας</h3>
            </body
        """
        # st.markdown(newhtml,unsafe_allow_html=True)
        st.write('Καλησπέρα, *%s*' % (name))
        perds=period_counter(names,periods,name)

        # st.set_page_config(layout="centered", page_icon="🎓", page_title="Diploma Generator")
        st.markdown(html3,unsafe_allow_html=True)

        st.markdown(html2,unsafe_allow_html=True)

        left, right = st.columns(2)

        # right.write("Here's the template we'll be using:")

        right.image("http://inclusiveeducation.eu/wp-content/uploads/2022/04/template.png", width=300)

        env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
        template = env.get_template("template.html")

        
        # left.write("Fill in the data:")
        form = left.form("template_form")
        student = name
        course="Report Generation in Streamlit"
        grade = 100
        period=perds
        submit = form.form_submit_button("Δημιουργία πιστοποιητικού")
        
        if submit:
            html = template.render(
                student=student,
                course=course,
                period=period,
                grade=f"{grade}/100",
                date=date.today().strftime("%B %d, %Y"),
            )

            pdf = pdfkit.from_string(html, False)
            st.balloons()

            right.success("🎉 Το πιστοποιητικό σας δημιουργήθηκε!")
            # st.write(html, unsafe_allow_html=True)
            # st.write("")
            right.download_button(
                "⬇️ Παραλαβή πιστοποιητικού",
                data=pdf,
                file_name="diploma.pdf",
                mime="application/octet-stream",
            )

elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')


# if st.session_state['authentication_status']:
#     st.write('Welcome *%s*' % (st.session_state['name']))
#     st.title('Some content')
elif st.session_state['authentication_status'] == False:
    st.error('Username/password is incorrect')
elif st.session_state['authentication_status'] == None:
    st.warning('Please enter your username and password')