# -*- coding: utf-8 -*-
"""PL — kopia oryginału (poza wiadomościami, w których PL był językiem oryginału)."""

SUBJ = {
0:"Wniosek o dostęp do dokumentów — sprawa M.10815",
1:"Potwierdzenie wpływu — numer sprawy 2025/6534",
2:"Odpowiedź — żądam nieocenzurowanej umowy",
3:"Pański wniosek o dostęp do dokumentów — sygn. EASE nr 2025/6534",
4:"Wniosek o przedłużenie terminu na złożenie wniosku potwierdzającego — sygn. EASE 2025/6534",
5:"Przedłużenie terminu 15 dni roboczych nie jest możliwe",
6:"Wniosek potwierdzający — art. 7 ust. 2 rozporządzenia (WE) nr 1049/2001",
7:"Wpływ potwierdzony — przekazano Sekretariatowi Generalnemu",
8:"Wewnętrzne rozpatrzenie wniosku o dostęp do dokumentów — Ares(2026)1214166",
9:"Wyjaśnienie proceduralne — wniosek potwierdzający złożony 26 stycznia 2026 r. (sprawa M.10815)",
10:"Automatyczne potwierdzenie — Dział Przejrzystości, Sekretariat Generalny",
11:"Strony podmiotów trzecich — proszę korzystać z oficjalnego portalu",
12:"Stanowisko proceduralne wnioskodawcy — przyjęcie i rozpatrzenie wniosku potwierdzającego",
13:"Automatyczne potwierdzenie — Dział Przejrzystości, Sekretariat Generalny",
14:"Złożenie zawiadomienia o przestępstwie — szkoda dla interesów finansowych UE (art. 325 TFUE)",
15:"Dokument uzupełniający",
16:"Odpowiedź na decyzję o odmowie dostępu do dokumentów — COMP/M.10815",
}

BADGE = {"Delivered":"Doręczono","Registered":"Zarejestrowano","Refused":"Odmowa",
         "Rejected as out of time":"Odrzucono jako spóźnione","Forwarded":"Przekazano",
         "Received":"Wpłynęło","Rejected":"Odrzucono"}

PHASES = {0:"Faza I — wniosek pierwotny", 3:"Faza II — pierwotna odmowa",
          6:"Faza III — wniosek potwierdzający", 14:"Faza IV — eskalacja"}

BODY = {}

BODY[0] = """
<p>Szanowna Dyrekcjo Generalna ds. Konkurencji,</p>
<p>na podstawie prawa dostępu do dokumentów wynikającego z traktatów UE, rozwiniętego w rozporządzeniu 1049/2001, wnoszę o udostępnienie dokumentów zawierających następujące informacje:</p>
<p>na podstawie <strong>rozporządzenia (WE) nr 1049/2001</strong>, <strong>art. 15 TFUE</strong> oraz <strong>art. 42 Karty praw podstawowych Unii Europejskiej</strong> wnoszę niniejszym o pełny dostęp do wszystkich dokumentów sprawy <strong>M.10815 – Deutsche Telekom / Orange / Telefónica / Vodafone – Joint Venture</strong>.</p>
<p>W szczególności wnoszę o dostęp do:</p>
<ul>
<li>pełnej umowy o wspólnym przedsiębiorstwie (nieocenzurowanej),</li>
<li>wszystkich załączników i aneksów do umowy o wspólnym przedsiębiorstwie,</li>
<li>umowy wspólników,</li>
<li>zasad ładu korporacyjnego i funkcjonowania wspólnego przedsiębiorstwa,</li>
<li>pełnej i nieocenzurowanej wersji decyzji Komisji,</li>
<li>zgłoszenia Form CO złożonego przez strony,</li>
<li>wszystkich analiz rynkowych i ocen wewnętrznych przeprowadzonych przez DG ds. Konkurencji,</li>
<li>całej korespondencji między DG ds. Konkurencji a stronami zgłaszającymi dotyczącej tego wspólnego przedsiębiorstwa.</li>
</ul>
<p>Ponieważ to wspólne przedsiębiorstwo zasadniczo wpływa na warunki konkurencji na rynku telekomunikacyjnym UE i dotyczy milionów obywateli Unii, uważam, że interes publiczny w przejrzystości wyraźnie przeważa nad ewentualnymi twierdzeniami o poufności handlowej, zgodnie z zasadami ustalonymi przez Trybunał Sprawiedliwości Unii Europejskiej.</p>
<p>Z poważaniem,<br>Peter Ferenc<br>Rammelkam 2, 84036 Kumhausen, Niemcy</p>"""

BODY[1] = """
<p>Szanowni Państwo,</p>
<p>niniejszym potwierdzamy wpływ Państwa wniosku o dostęp do dokumentów przesłanego 10.12.2025 r. i zarejestrowanego 10.12.2025 r. pod numerem sprawy <strong>2025/6534</strong>.</p>
<p>Wniosek rozpatrzymy w terminie <strong>15 dni roboczych</strong> od daty rejestracji. Termin upływa <strong>12.01.2026 r.</strong> Poinformujemy Państwa, jeżeli konieczne będzie przedłużenie go o kolejne 15 dni roboczych.</p>
<p>Więcej informacji o przetwarzaniu Państwa danych osobowych znajduje się w oświadczeniu o ochronie prywatności.</p>
<p>Z poważaniem,<br>Dyrekcja Generalna ds. Konkurencji – Dostęp do dokumentów<br>Komisja Europejska</p>"""

BODY[2] = """
<p>Szanowna Dyrekcjo Generalna ds. Konkurencji,</p>
<p>dziękuję, czekam na Państwa odpowiedź! Żądam nieocenzurowanej, przejrzystej umowy!</p>
<p>Z poważaniem,<br>Peter Ferenc</p>"""

BODY[3] = """
<p>Szanowny Panie Ferenc,</p>
<p><strong>Dotyczy:</strong> Pański wniosek o dostęp do dokumentów – sygn. EASE nr 2025/6534</p>
<p>Nawiązujemy do Pańskiej wiadomości z 10.12.2025 r., w której składa Pan wniosek o dostęp do dokumentów, zarejestrowany 10.12.2025 r. pod wyżej wymienionym numerem.</p>
<p>W załączeniu przesyłamy skan odpowiedzi na Pański wniosek o dostęp do dokumentów, <strong>podpisanej przez dyrektora generalnego</strong>.</p>
<p>Uprzejmie prosimy o odpowiedź na niniejszą wiadomość i potwierdzenie jej otrzymania.</p>
<p>Z poważaniem,</p>
<p>Komisja Europejska<br>Dyrekcja Generalna ds. Konkurencji<br>Dział C.5 Koncentracje<br>Dyrekcja C – Rynki i sprawy: technologie informacyjne, komunikacja i media</p>"""

BODY[4] = """
<p>Szanowni Państwo,</p>
<p>niniejszym formalnie wnoszę o przedłużenie terminu na złożenie wniosku potwierdzającego w związku z moim wnioskiem o dostęp do dokumentów zarejestrowanym pod sygnaturą EASE 2025/6534.</p>
<p><strong>Uzasadnienie wniosku</strong></p>
<p>Z obiektywnych przyczyn technicznych nie mam obecnie niezawodnego dostępu do wszystkich środków technicznych i danych uwierzytelniających niezbędnych do przygotowania i złożenia prawnie uzasadnionego wniosku potwierdzającego.</p>
<p>Zakres i złożoność podstaw odmowy wymagają gruntownej analizy prawnej i faktycznej, w szczególności w odniesieniu do:</p>
<ul>
<li>zastosowania wyjątków od prawa dostępu do dokumentów,</li>
<li>proporcjonalności dokonanych zaczernień,</li>
<li>oraz oceny zgodności z prawem Unii.</li>
</ul>
<p>Złożenie wniosku potwierdzającego bez takiej analizy byłoby czysto formalne i podważyłoby sam cel środka prawnego przewidzianego w prawie Unii.</p>
<p><strong>Podstawa prawna</strong></p>
<p>Wniosek opiera się między innymi na:</p>
<ul>
<li>art. 41 Karty praw podstawowych Unii Europejskiej (prawo do dobrej administracji),</li>
<li>art. 47 Karty praw podstawowych Unii Europejskiej (prawo do skutecznego środka prawnego),</li>
<li>zasadzie równości broni i skutecznego wykonywania praw procesowych,</li>
<li>oraz utrwalonym orzecznictwie, zgodnie z którym terminy procesowe nie mogą być stosowane w sposób czyniący wykonywanie praw przyznanych prawem Unii praktycznie niemożliwym lub nadmiernie utrudnionym.</li>
</ul>
<p><strong>Żądanie</strong></p>
<p>Wobec powyższego wnoszę o przedłużenie o <strong>30 dni</strong>, liczone od upływu pierwotnego terminu na złożenie wniosku potwierdzającego.</p>
<p>Niniejszy wniosek składam bez jakiegokolwiek zrzeczenia się praw ani przyznania opóźnienia, wyłącznie w celu zapewnienia prawidłowego, świadomego i prawnie skutecznego wykonania mojego prawa do środka prawnego.</p>
<p>Uprzejmie proszę o pisemne potwierdzenie, czy przedłużenie zostało udzielone.</p>
<p>Z poważaniem,<br>Peter Ferenc</p>"""

BODY[5] = """
<p>Szanowny Panie Ferenc,</p>
<p>dziękujemy za wiadomość z 19 stycznia 2026 r., w której pyta Pan, czy możliwe jest przedłużenie ustawowego terminu 15 dni roboczych przewidzianego w art. 7 ust. 2 rozporządzenia 1049/2001 na złożenie wniosku potwierdzającego w odpowiedzi na częściową lub całkowitą odmowę udzielenia dostępu do dokumentów.</p>
<p>Informujemy, że <strong>przedłużenie tego terminu 15 dni roboczych nie jest możliwe</strong>, ponieważ terminy określone w rozporządzeniu 1049/2001 nie pozostają w dyspozycji stron i mają charakter rozstrzygający dla postępowania w sprawie dostępu do dokumentów będących w posiadaniu instytucji.</p>
<p>W tym kontekście zwracamy uwagę, że <strong>etap wniosku potwierdzającego stanowi pełne rozpatrzenie administracyjne decyzji pierwotnej i musi naprawić każde jej uchybienie, nawet jeśli wnioskodawca nie zakwestionował go wyraźnie we wniosku potwierdzającym</strong>.</p>
<p>Ponieważ termin na złożenie wniosku potwierdzającego wobec pierwotnej odmownej odpowiedzi Dyrekcji Generalnej ds. Konkurencji z 7 stycznia 2026 r. na Pański wniosek o dostęp do dokumentów z 10 grudnia 2025 r., zarejestrowany pod sygnaturą EASE 2025/6534, <strong>jeszcze nie upłynął</strong>, informujemy, że Pańskiego zapytania nie traktujemy w związku z tym jako takiego wniosku potwierdzającego w rozumieniu rozporządzenia 1049/2001.</p>
<p>W tym zakresie ponownie odsyłamy do sekcji 5 naszej pierwotnej odmownej odpowiedzi z 7 stycznia 2026 r., w której wyjaśniliśmy dostępne środki zaskarżenia, obowiązujący termin ustawowy oraz sposób i służbę Komisji Europejskiej, do której ewentualnie należy taki wniosek potwierdzający złożyć.</p>
<p>Z wyrazami szacunku,</p>
<p>Komisja Europejska<br>Dyrekcja Generalna ds. Konkurencji<br>Dział C.5 Koncentracje<br>Dyrekcja C – Rynki i sprawy: technologie informacyjne, komunikacja i media</p>"""

BODY[6] = """
<p>Szanowni Państwo,</p>
<p>niniejszy wniosek potwierdzający został już złożony <strong>26 stycznia 2026 r.</strong> za pośrednictwem platformy AskTheEU. Wskutek błędu technicznego wysłano go przez niewłaściwy interfejs i nie dotarł do instytucji.</p>
<p>Zespół AskTheEU / Access Info Europe potwierdził na piśmie, że wiadomość została złożona w terminie, i w razie potrzeby może to poświadczyć. Poniżej link do dokumentu potwierdzającego terminowe złożenie mojego wniosku potwierdzającego kanałem alternatywnym, wskutek błędu technicznego platformy.</p>
<p>Niniejszym składam wniosek potwierdzający na podstawie <strong>art. 7 ust. 2 rozporządzenia (WE) nr 1049/2001</strong> i wnoszę o pełne rozpatrzenie administracyjne pierwotnej odmownej odpowiedzi z 7 stycznia 2026 r. wydanej przez Dyrekcję Generalną ds. Konkurencji na mój wniosek o dostęp do dokumentów z 10 grudnia 2025 r., zarejestrowany pod sygnaturą EASE 2025/6534.</p>
<p>Podtrzymuję, że decyzja pierwotna bezprawnie ogranicza moje prawo dostępu do dokumentów i nie odpowiada zasadom przejrzystości, proporcjonalności i dobrej administracji określonym w rozporządzeniu 1049/2001 i art. 15 TFUE.</p>
<p>W szczególności:</p>
<p><strong>1. Nieprawidłowe lub zbyt szerokie zastosowanie wyjątków</strong><br>
Odpowiedź pierwotna opiera się na wyjątkach, co do których nie wykazano, że mają zastosowanie konkretnie i indywidualnie do żądanych dokumentów. Przedstawione uzasadnienie pozostaje abstrakcyjne i nie wykazuje, w jaki sposób ujawnienie miałoby konkretnie i rzeczywiście naruszyć chroniony interes, czego wymaga utrwalone orzecznictwo Trybunału Sprawiedliwości.</p>
<p><strong>2. Brak właściwej oceny nadrzędnego interesu publicznego</strong><br>
Żądane dokumenty dotyczą spraw o istotnym znaczeniu publicznym, w tym funkcjonowania egzekwowania prawa konkurencji, przestrzegania prawa Unii i ochrony praw podstawowych. Decyzja pierwotna nie zawiera rzeczywistej i uzasadnionej oceny, czy istnieje nadrzędny interes publiczny w ujawnieniu.</p>
<p><strong>3. Niedostateczne uzasadnienie i brak indywidualnego badania</strong><br>
Odmowa nie wykazuje, że każdy dokument został zbadany indywidualnie, ani nie wyjaśnia, dlaczego nie można było udzielić dostępu częściowego zgodnie z art. 4 ust. 6 rozporządzenia 1049/2001.</p>
<p><strong>4. Znaczenie ochrony danych i zgodności z RODO</strong><br>
W zakresie, w jakim powołano się na względy ochrony danych, zauważam, że rozporządzenie (UE) 2018/1725 i rozporządzenie (UE) 2016/679 (RODO) nie uzasadniają odmowy o charakterze blankietowym. Wszelkie kwestie danych osobowych mogą i powinny zostać rozwiązane przez odpowiednie zaczernienie, a nie przez odmowę dostępu.</p>
<p>Jak przypominają Państwo w piśmie z 20 stycznia 2026 r., etap wniosku potwierdzającego stanowi pełne rozpatrzenie administracyjne decyzji pierwotnej. Wzywam zatem Komisję do ponownego rozpatrzenia wniosku w całości i do naprawienia wszelkich uchybień lub błędów zawartych w odpowiedzi pierwotnej, w tym tych, których wyżej wyraźnie nie zakwestionowałem.</p>
<p>Wnoszę, aby Komisja udzieliła dostępu do żądanych dokumentów w całości lub co najmniej częściowo, zgodnie z rozporządzeniem 1049/2001.</p>
<p>Z poważaniem,<br>Peter Ferenc</p>"""

BODY[7] = """
<p>Szanowny Panie Ferenc,</p>
<p>niniejszym potwierdzamy wpływ Pańskiej wiadomości z 30 stycznia 2026 r., w której składa Pan wniosek o decyzję potwierdzającą.</p>
<p>Informujemy, że <strong>przekazaliśmy Pańską wiadomość właściwemu Sekretariatowi Generalnemu Komisji Europejskiej</strong>.</p>
<p>Z wyrazami szacunku<br>COMP C-5</p>"""

BODY[8] = """
<p>Szanowny Wnioskodawco,</p>
<p>nawiązuję do Pańskiej wiadomości z 30 stycznia 2026 r., w której składa Pan wniosek potwierdzający zgodnie z art. 7 ust. 2 rozporządzenia 1049/2001 w sprawie publicznego dostępu do dokumentów Parlamentu Europejskiego, Rady i Komisji (dalej: rozporządzenie 1049/2001).</p>
<p>Z przykrością informuję, że <strong>Pański wniosek potwierdzający został złożony po upływie terminu</strong> określonego w art. 7 ust. 2 rozporządzenia 1049/2001. Przepis ten stanowi, że w przypadku całkowitej lub częściowej odmowy wnioskodawca może w terminie 15 dni roboczych od otrzymania odpowiedzi instytucji złożyć wniosek potwierdzający, w którym zwraca się do instytucji o ponowne rozpatrzenie jej stanowiska.</p>
<p><strong>Komisja nie jest zatem w stanie rozpatrzyć Pańskiego wniosku.</strong></p>
<p>Z poważaniem,<br>Komisja Europejska<br>Zespół ds. Dostępu do Dokumentów</p>"""

BODY[9] = """
<p>Szanowni Państwo,</p>
<p>muszę formalnie sprzeciwić się stanowisku obecnie prezentowanemu w tej sprawie i wnoszę o rzetelne odzwierciedlenie stanu faktycznego i proceduralnego.</p>
<p><strong>1. Terminowe złożenie wniosku potwierdzającego</strong><br>
Mój wniosek potwierdzający na podstawie art. 7 ust. 2 rozporządzenia (WE) nr 1049/2001 został <strong>w pełni sporządzony i złożony 26 stycznia 2026 r.</strong>, tj. <strong>w ostatnim dniu terminu ustawowego</strong>, za pośrednictwem platformy AskTheEU. Fakt ten <strong>nie jest sporny</strong> i został <strong>wyraźnie potwierdzony na piśmie przez Access Info Europe</strong>, wraz z dowodem dokumentowym (opatrzone znacznikiem czasu potwierdzenie wpływu mojej wiadomości 26 stycznia 2026 r.).</p>
<p><strong>2. Technicznego nieprzekazania nie można przypisać wnioskodawcy</strong><br>
Ewentualny brak przekazania wniosku potwierdzającego Komisji wynikał wyłącznie z problemu technicznego i organizacyjnego po stronie platformy pośredniczącej. Zgodnie z utrwalonym orzecznictwem i ogólnymi zasadami prawa Unii:</p>
<ul>
<li>wnioskodawca <strong>nie może zostać ukarany</strong> za awarie techniczne platformy pośredniczącej użytej w dobrej wierze;</li>
<li>prawa procesowe przyznane rozporządzeniem 1049/2001 <strong>nie mogą wygasnąć wskutek nadmiernego formalizmu</strong>.</li>
</ul>
<p><strong>3. Uzasadnione oczekiwania i przyjęcie proceduralne</strong><br>
Istotne jest, że wniosek potwierdzający został przyjęty, rozpatrzony wewnętrznie i przekazany właściwym służbom Komisji. Czynności te stanowią <strong>formalne kroki proceduralne</strong>, które <strong>w sposób dorozumiany uznały ważność proceduralną</strong> wniosku potwierdzającego. Skoro takie przyjęcie proceduralne już nastąpiło, <strong>prawnie niedopuszczalne</strong> jest jego wsteczne zanegowanie, gdyż naruszałoby to:</p>
<ul>
<li>zasadę dobrej administracji (art. 41 Karty),</li>
<li>ochronę uzasadnionych oczekiwań,</li>
<li>oraz skuteczność prawa Unii.</li>
</ul>
<p><strong>4. Konsekwencje</strong><br>
Każda próba przekwalifikowania prawidłowo złożonego wniosku potwierdzającego na „spóźniony" stanowiłaby arbitralne działanie administracyjne, oczywiście nieproporcjonalny formalizm oraz naruszenie art. 41 i 47 Karty praw podstawowych. Takie postępowanie podlegałoby <strong>odrębnej kontroli</strong> Europejskiego Rzecznika Praw Obywatelskich, a w razie potrzeby sądów Unii.</p>
<p><strong>5. Żądanie</strong><br>
Wnoszę zatem, aby:</p>
<ul>
<li>akta zostały sprostowane tak, by odzwierciedlały terminowe złożenie 26 stycznia 2026 r.,</li>
<li>wniosek potwierdzający został potraktowany jako skutecznie złożony,</li>
<li>a Komisja przeprowadziła pełne rozpatrzenie administracyjne wymagane art. 7 ust. 2 rozporządzenia 1049/2001.</li>
</ul>
<p>Niniejsze pismo składam <strong>dla uniknięcia wątpliwości i bez uszczerbku</strong> dla wszelkich dalszych środków prawnych przysługujących mi na mocy prawa Unii.</p>
<p><strong>Dodatkowe wyjaśnienie proceduralne</strong><br>
Dla uniknięcia wszelkich wątpliwości potwierdzam, że ten sam wniosek potwierdzający został <strong>7 lutego 2026 r.</strong> przekazany również bezpośrednio Komisji Europejskiej oficjalnymi kanałami poczty elektronicznej, a także gabinetowi członka Komisji. Treść wniosku potwierdzającego została zatem jednoznacznie udostępniona Komisji wieloma oficjalnymi kanałami, co dodatkowo świadczy o mojej dobrej wierze, współpracy proceduralnej i rzeczywistym zamiarze wykonywania moich praw z rozporządzenia (WE) nr 1049/2001 w sposób prawidłowy i staranny.</p>
<p>Z poważaniem,<br>Peter Ferenc<br>Sygn.: TFIA-2026-JV-002</p>"""

BODY[10] = """
<p>Państwa wiadomość wpłynęła do Działu Przejrzystości Sekretariatu Generalnego Komisji Europejskiej.</p>
<p>Wnioski o publiczny dostęp do dokumentów rozpatrywane są na podstawie rozporządzenia (WE) nr 1049/2001 z dnia 30 maja 2001 r. w sprawie publicznego dostępu do dokumentów Parlamentu Europejskiego, Rady i Komisji.</p>
<p>Sekretariat Generalny odpowie na Państwa wniosek w terminie <strong>15 dni roboczych</strong> od jego rejestracji i należycie poinformuje o rejestracji wniosku (lub o dodatkowych informacjach, które należy przedstawić w celu jego rejestracji lub rozpatrzenia).</p>
<p><em>Ten sam tekst nastąpił po angielsku, francusku i niemiecku.</em></p>"""

BODY[11] = """
<p>Szanowny Wnioskodawco,</p>
<p><strong>Komisja Europejska nie może ponosić odpowiedzialności za problemy ze stronami podmiotów trzecich.</strong> Zachęcamy do korzystania z oficjalnego portalu do składania wniosków o dokumenty Komisji Europejskiej.</p>
<p>Z wyrazami szacunku,<br>Komisja Europejska<br>Zespół ds. Dostępu do Dokumentów</p>"""

BODY[12] = """
<p>Szanowni Państwo,</p>
<p>przyjmuję do wiadomości Państwa oświadczenie, zgodnie z którym Komisja Europejska nie może ponosić odpowiedzialności za techniczne funkcjonowanie stron podmiotów trzecich, takich jak platforma AskTheEU. <strong>Nie mogę zgodzić się z tym twierdzeniem.</strong></p>
<p>Platforma AskTheEU jest od dawna akceptowana, wykorzystywana i faktycznie stosowana przez Komisję Europejską jako standardowe narzędzie wykonywania publicznego prawa dostępu do dokumentów; za jej pośrednictwem Komisja:</p>
<ul>
<li>regularnie przyjmuje i rozpatruje wnioski o dostęp do dokumentów,</li>
<li>komunikuje się z wnioskodawcami oraz</li>
<li>systematycznie przetwarza pisma na podstawie rozporządzenia (WE) nr 1049/2001.</li>
</ul>
<p>W tych okolicznościach AskTheEU nie można uznać za przypadkowy lub nieuprawniony podmiot trzeci, z którego korzystanie odbywałoby się na własne ryzyko wnioskodawcy.</p>
<p>Niezależnie od powyższego podkreślam, że kwestia ta nie jest rozstrzygająca dla oceny dopuszczalności proceduralnej mojego pisma. <strong>Rozstrzygające jest to, że Komisja Europejska otrzymała mój wniosek potwierdzający, potwierdziła jego wpływ i rozpoczęła jego rozpatrywanie</strong>, co wyraźnie potwierdziła wiadomość Działu Przejrzystości Sekretariatu Generalnego.</p>
<p>Od chwili, w której Komisja otrzymała pismo, umieściła je w ramach rozporządzenia (WE) nr 1049/2001 i poinformowała mnie, że zostanie rozpatrzone w terminie ustawowym od rejestracji, <strong>powstał formalny stosunek proceduralny między wnioskodawcą a instytucją</strong>, za który pełną odpowiedzialność ponosi wyłącznie Komisja Europejska.</p>
<p>Kwestia kanału, którym pismo zostało pierwotnie przekazane, nie może wstecznie wpływać na jego dopuszczalność proceduralną, tym bardziej że sama Komisja potwierdziła wpływ i rozpoczęcie rozpatrywania.</p>
<p>W tych okolicznościach prawnie niedopuszczalne jest następcze kwestionowanie terminowości lub dopuszczalności wniosku potwierdzającego ani przenoszenie na wnioskodawcę skutków ustaleń technicznych lub umownych między Komisją a podmiotem trzecim.</p>
<p>Wnoszę zatem, aby Komisja przeprowadziła pełne rozpatrzenie administracyjne wniosku potwierdzającego zgodnie z art. 7 ust. 2 rozporządzenia (WE) nr 1049/2001.</p>
<p>Z poważaniem,<br>Peter Ferenc</p>"""

BODY[13] = """
<p>Państwa wiadomość wpłynęła do Działu Przejrzystości Sekretariatu Generalnego Komisji Europejskiej.</p>
<p>Wnioski o publiczny dostęp do dokumentów rozpatrywane są na podstawie rozporządzenia (WE) nr 1049/2001 z dnia 30 maja 2001 r. w sprawie publicznego dostępu do dokumentów Parlamentu Europejskiego, Rady i Komisji.</p>
<p>Sekretariat Generalny odpowie na Państwa wniosek w terminie 15 dni roboczych od jego rejestracji i należycie poinformuje o rejestracji.</p>
<p><em>Ten sam tekst nastąpił po angielsku, francusku i niemiecku.</em></p>"""

BODY[14] = """
<p>Szanowni Państwo,</p>
<p>niniejszym przekazuję zawiadomienie o podejrzeniu popełnienia przestępstwa w formie linku.</p>
<p>Zawiadomienie dotyczy podejrzenia przestępstw naruszających interesy finansowe Unii Europejskiej w rozumieniu <strong>art. 325 TFUE</strong> oraz <strong>dyrektywy (UE) 2017/1371 (PIF)</strong>.</p>
<p>Zawiadomienie zostało sporządzone jako dokument PDF podpisany <strong>kwalifikowanym podpisem elektronicznym (QES)</strong>, który zgodnie z art. 25 ust. 2 rozporządzenia (UE) nr 910/2014 (eIDAS) wywołuje takie same skutki prawne jak podpis własnoręczny.</p>
<p>Złożenie następuje w języku słowackim, który jest językiem urzędowym Unii Europejskiej. <strong>Słowacka wersja językowa jest uznawana za wersję oryginalną i prawnie wiążącą.</strong> Wersje EN → DE → FR → ES → PL → IT są dołączone wyłącznie jako wierne tłumaczenia lustrzane, w celu ułatwienia rozpatrzenia.</p>
<p>Wyraźnie wskazuję, że <strong>prawo Unii nie nakłada obowiązku składania zawiadomienia za pośrednictwem określonego formularza online</strong>. Zgodnie z art. 24 rozporządzenia Rady (UE) 2017/1939 Prokuratura Europejska może przyjmować informacje o przestępstwach naruszających interesy finansowe Unii z każdego źródła, w tym od osób fizycznych.</p>
<p>Jakiekolwiek ograniczenia techniczne lub proceduralne, które:</p>
<ul>
<li>uniemożliwiałyby przekazanie pełnej treści,</li>
<li>wymuszałyby jej skrócenie lub prowadziły do utraty twierdzeń faktycznych lub dowodów,</li>
<li>lub uzależniałyby przyjęcie od dodatkowej „wstępnej oceny",</li>
</ul>
<p>stanowiłyby nielegalną barierę dostępu do wymiaru sprawiedliwości oraz naruszenie art. 47 Karty praw podstawowych UE i art. 13 EKPC.</p>
<p>Oczekuję zatem, że zawiadomienie zostanie prawidłowo zarejestrowane, rozpatrzone i ocenione merytorycznie, zgodnie z prawem Unii Europejskiej, niezależnie od technicznego sposobu jego przekazania.</p>
<p>Z poważaniem,<br>Peter Ferenc<br>Kumhausen, 11.02.2026</p>
<p><em>Identyczny tekst przekazano w tej samej wiadomości również po EN, DE, FR, ES, IT i SK.</em></p>"""

BODY[15] = """
<p>Szanowny Zespole AskTheEU,</p>
<p>[link do podpisanego dokumentu]</p>
<p>Z poważaniem,<br>Peter Ferenc</p>"""

BODY[16] = """
<p>Szanowna Pani Dyrektor Generalna, Szanowny Panie Whelan,</p>
<p>w załączeniu przesyłam moją odpowiedź na Państwa decyzję z 7 stycznia 2026 r., którą odmówiono mi dostępu do dokumentów akt sprawy COMP/M.10815. Dokument opatrzony jest <strong>kwalifikowanym podpisem elektronicznym (QES)</strong> zgodnie z art. 25 ust. 2 rozporządzenia eIDAS (nr 910/2014) i jest prawnie równoważny podpisowi własnoręcznemu.</p>
<p>Dostęp do dokumentów instytucji nie jest kwestią uznania Komisji. Zgodnie z <strong>art. 15 ust. 3 TFUE</strong>, <strong>art. 42 Karty praw podstawowych UE</strong> i <strong>art. 2 ust. 1 rozporządzenia (WE) nr 1049/2001</strong> każdy obywatel Unii ma prawo dostępu do dokumentów instytucji bez konieczności wykazywania interesu lub powodu. Odmowa jest wyjątkiem; zgodnie z utrwalonym orzecznictwem Trybunału podlega wykładni ścisłej, a <strong>ciężar dowodu spoczywa na instytucji, a nie na wnioskodawcy</strong>.</p>
<p>W mojej odpowiedzi wskazuję pięć powodów, dla których decyzja nie może się ostać:</p>
<p><strong>1.</strong> Termin obliczyli Państwo od daty odpowiedzi, mimo że art. 7 ust. 2 rozporządzenia wiąże go z otrzymaniem. Ponadto: 20 stycznia 2026 r. poinformowali mnie Państwo na piśmie, że termin jeszcze nie upłynął; 30 stycznia dział COMP C-5 potwierdził wpływ i przekazał pismo Sekretariatowi Generalnemu; 3 lutego odrzucono je jako spóźnione. <strong>Te trzy czynności wzajemnie sobie przeczą.</strong></p>
<p><strong>2.</strong> Ogólne domniemanie nieujawniania sami Państwo określają jako wzruszalne, a jednocześnie zarzucają mi, że nie wykazałem przeciwieństwa — odmawiając mi wglądu choćby w spis akt. <strong>Domniemanie, którego nie można obalić, nie jest domniemaniem wzruszalnym</strong> (Odile Jacob, C-404/10 P; Agrofert, C-477/10 P).</p>
<p><strong>3.</strong> Domniemanie nie obejmuje ani wewnętrznych analiz rynkowych DG ds. Konkurencji, ani nieocenzurowanej wersji samej decyzji — są to akty instytucji, a nie pisma stron. Państwa decyzja nie zawiera indywidualnego badania tych kategorii.</p>
<p><strong>4.</strong> Dostępu częściowego na podstawie art. 4 ust. 6 Państwo nie ocenili; odsyłają mnie Państwo do dokumentów, które są publiczne również bez Państwa decyzji.</p>
<p><strong>5.</strong> Nadrzędny interes publiczny odrzucili Państwo jako rozważania natury ogólnej, mimo że odwołałem się do <strong>motywów 138–142 Państwa własnej decyzji M.10815</strong>, w których Komisja sama stwierdza, że nie badała zgodności stron z RODO.</p>
<p>Wzywam Państwa do merytorycznego rozpatrzenia wniosku, przekazania mi spisu akt oraz zbadania każdego żądanego dokumentu konkretnie i indywidualnie. Jeżeli Komisja nie odniesie się merytorycznie do niniejszej odpowiedzi, zastrzegam sobie:</p>
<ul>
<li>skargę do <strong>Europejskiego Rzecznika Praw Obywatelskich</strong> z powodu niewłaściwego administrowania;</li>
<li>wniesienie <strong>skargi na podstawie art. 263 TFUE</strong>.</li>
</ul>
<p>Zastrzeżenie to wywołuje skutek prawny od chwili doręczenia niniejszego pisma.</p>
<p>Z wyrazami szacunku,<br>Peter Ferenc</p>
<p><em>Identyczny tekst przekazano w tej samej wiadomości również po niemiecku i angielsku.</em></p>"""
