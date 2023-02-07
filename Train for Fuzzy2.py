import pandas as pd
from tqdm import tqdm
import spacy
from spacy.tokens import DocBin

nlp = spacy.blank("en") 
db = DocBin() 

TRAIN_DATA = [("alaffia balancing day cream",{"entities":[(0,7,"brand"),(8,17,"desc"),(18,21,"desc"),(22,27,"product")]}),
("alba botanica sensitive fragrance free mineral sunscreen lotion",{"entities":[(0,13,"brand"),(14,24,"desc"),(24,34,"desc"),(34,39,"desc"),(39,46,"desc"),(47,57,"product"),(57,63,"product")]}),
("allies of skin vitamin c serum",{"entities":[(0,14,"brand"),(15,24,"desc"),(25,30,"product")]}),
("alpha lipoic acid 5% by the ordinary",{"entities":[(0,5,"brand"),(6,13,"desc"),(13,18,"desc"),(24,36,"product")]}),
("alpha skin care dual action skin lightener",{"entities":[(0,5,"brand"),(6,15,"desc"),(16,20,"desc"),(21,27,"desc"),(28,32,"desc"),(33,42,"product")]}),
("aquaphor healing ointment",{"entities":[(0,8,"brand"),(9,16,"desc"),(17,25,"product")]}),
("aquaphor lip repair ointment",{"entities":[(0,8,"brand"),(9,12,"desc"),(13,19,"desc"),(20,28,"product")]}),
("australian gold botanical tinted face sunscreen spf 50",{"entities":[(0,15,"brand"),(16,25,"desc"),(26,32,"desc"),(33,37,"desc"),(38,47,"product"),(48,54,"desc")]}),
("aveeno calm + restore oat gel face moisturizer, sensitive skin",{"entities":[(0,6,"brand"),(7,21,"desc"),(22,25,"desc"),(26,29,"desc"),(30,34,"desc"),(35,46,"product"),(48,62,"desc")]}),
("aveeno therapeutic shave gel",{"entities":[(0,6,"brand"),(7,18,"desc"),(19,24,"desc"),(25,28,"product")]}),
("avene skin recovery cream",{"entities":[(0,5,"brand"),(6,10,"desc"),(11,19,"desc"),(20,25,"product")]}),
("banila clean it zero purity",{"entities":[(0,6,"brand"),(7,12,"desc"),(13,15,"desc"),(16,20,"desc"),(21,27,"desc")]}),
("bioderma sensibio h2o",{"entities":[(0,8,"brand"),(9,21,"name")]}),
("biore uv aqua rich watery essence spf 50 pa+++",{"entities":[(0,5,"brand"),(6,8,"desc"),(9,13,"desc"),(14,18,"desc"),(19,23,"desc"),(19,25,"desc"),(26,32,"product"),(26,33,"product"),(34,46,"desc")]}),
("blue lizard face mineral based sunscreen with hydrating hyaluronic acid spf 30+ uva/uvb protection",{"entities":[(0,11,"brand"),(12,16,"desc"),(17,24,"desc"),(25,30,"desc"),(31,40,"product"),(46,55,"desc"),(56,66,"desc"),(67,71,"desc"),(72,78,"desc"),(80,87,"desc"),(88,98,"desc")]}),
("burt's bees lavender and honey lip butter",{"entities":[(0,11,"brand"),(12,20,"desc"),(25,30,"desc"),(31,34,"desc"),(35,41,"product")]}),
("cerave healing ointment ",{"entities":[(0,6,"brand"),(7,14,"desc"),(15,23,"product")]}),
("cerave hydrating cleanser", {"entities":[(0,6,"brand"),(7,16,"desc"),(17,25,"product")]}),
("cetaphil restoraderm eczema calming body wash",{"entities":[(0,8,"brand"),(9,20,"desc"),(21,27,"desc"),(28,35,"desc"),(36,40,"desc"),(41,45,"product")]}),
("clean & clear persa gel 10",{"entities":[(0,13,"brand"),(14,19,"desc"),(20,23,"product"),(24,26,"desc")]}),
("clinique dramatically different moisturizing gel",{"entities":[(0,8,"brand"),(9,21,"desc"),(22,31,"desc"),(32,44,"desc"),(45,48,"product")]}),
("colorescience sunforgettable total protection face shield classic spf 50",{"entities":[(0,13,"brand"),(14,28,"desc"),(29,34,"desc"),(35,45,"desc"),(46,50,"desc"),(51,57,"desc"),(58,65,"desc"),(66,69,"desc"),(0,0,"desc"),(70,72,"desc")]}),
("cosrx snail 92 all in one cream",{"entities":[(0,5,"brand"),(6,11,"desc"),(12,14,"desc"),(15,25,"desc"),(26,31,"product")]}),
("dr. hauschka cleansing cream",{"entities":[(0,12,"brand"),(13,22,"desc"),(23,28,"product")]}),
("dr. loretta gentle hydrating cleanser",{"entities":[(0,11,"brand"),(12,18,"desc"),(19,28,"desc"),(29,37,"product")]}),
("dr. song 2.5% benzoyl peroxide advanced acne gel",{"entities":[(0,8,"brand"),(9,13,"desc"),(14,21,"desc"),(22,30,"desc"),(31,39,"desc"),(40,44,"desc"),(0,0,"product"),(45,48,"product")]}),
("drunk elephant peekee bar",{"entities":[(0,14,"brand"),(15,21,"desc"),(22,25,"product")]}),
("e.l.f. holy hydration fragrance free face cream",{"entities":[(0,6,"brand"),(7,11,"desc"),(12,21,"desc"),(22,31,"desc"),(32,35,"desc"),(32,36,"desc"),(37,41,"desc"),(42,47,"product")]}),
("e.l.f. lip exfoliator",{"entities":[(0,6,"brand"),(7,10,"desc"),(11,21,"product")]}),
("elizavecca milky piggy carbonated bubble clay mask",{"entities":[(0,10,"brand"),(11,16,"desc"),(17,22,"desc"),(23,33,"desc"),(34,40,"desc"),(41,45,"desc"),(46,50,"product")]}),
("eltamd uv clear broad spectrum spf 46",{"entities":[(0,6,"brand"),(7,9,"desc"),(10,15,"desc"),(16,21,"desc"),(22,30,"desc"),(31,34,"desc")]}),
("etude house soon jung 10 free moist emulsion",{"entities":[(0,11,"brand"),(12,21,"desc"),(25,29,"desc"),(30,35,"desc"),(36,44,"product")]}),
("etude house soon jung ph 6.5 whip cleanser",{"entities":[(0,11,"brand"),(12,21,"desc"),(22,24,"desc"),(29,33,"desc"),(34,42,"product")]}),
("eucerin ph 5 skin protection shower oil",{"entities":[(0,7,"brand"),(8,10,"desc"),(13,17,"desc"),(18,28,"desc"),(29,35,"desc"),(36,39,"product")]}),
("evan healy whipped shea butter for lips",{"entities":[(0,10,"brand"),(11,18,"desc"),(19,23,"desc"),(24,30,"product"),(35,39,"desc")]}),
("farmacy green clean make up removing cleansing balm",{"entities":[(0,13,"brand"),(14,19,"desc"),(20,27,"desc"),(28,36,"desc"),(37,46,"desc"),(47,51,"product")]}),
("first aid beauty pure skin face cleanser",{"entities":[(0,16,"brand"),(17,21,"desc"),(22,26,"desc"),(27,31,"desc"),(32,40,"product")]}),
("first aid beauty ultra repair cream",{"entities":[(0,16,"brand"),(17,22,"desc"),(23,29,"desc"),(30,35,"product")]}),
("freeman avocado & oatmeal facial clay mask",{"entities":[(0,7,"brand"),(8,15,"desc"),(18,25,"desc"),(26,32,"desc"),(33,37,"desc"),(38,42,"product")]}),
("fresh soy face cleanser",{"entities":[(0,5,"brand"),(6,9,"desc"),(10,14,"desc"),(15,23,"product")]}),
#40
("garden of wisdom 8% azelaic serum azelaic acid %: 8%",{"entities":[(0,16,"brand"),(17,19,"desc"),(20,27,"desc"),(28,33,"product"),(34,41,"desc"),(42,46,"desc"),(50,52,"desc")]}),
("garnier skin active micellar foaming gel cleanser",{"entities":[(0,7,"brand"),(8,12,"desc"),(13,19,"desc"),(20,28,"desc"),(29,36,"desc"),(37,40,"product"),(41,49,"product")]}),
("glossier balm dotcom",{"entities":[(0,8,"brand"),(9,13,"product"),(14,20,"desc")]}),
("gloves in a bottle sheilding lotion ",{"entities":[(0,18,"brand"),(19,28,"desc"),(29,35,"product")]}),
("glow recipe watermelon glow sleeping mask",{"entities":[(0,11,"brand"),(12,22,"desc"),(28,36,"desc"),(37,41,"product")]}),
("hada labo goku jyun foaming face wash",{"entities":[(0,9,"brand"),(10,19,"desc"),(20,27,"desc"),(28,32,"desc"),(33,37,"product")]}),
("hada labo tokyo anti aging facial sheet masks",{"entities":[(0,9,"brand"),(10,15,"desc"),(16,26,"desc"),(27,33,"desc"),(34,39,"product"),(40,45,"product")]}),
("heimish cleansing balm ",{"entities":[(0,7,"brand"),(8,17,"desc"),(18,23,"product")]}),
("isehan kiss me mommy uv aqua milk waterproof sunscreen spf 50+ pa++++",{"entities":[(0,6,"brand"),(21,23,"desc"),(24,28,"desc"),(34,44,"desc"),(29,33,"product"),(45,54,"product"),(55,69,"desc")]}),
("jergens natural glow moisturizer",{"entities":[(0,7,"brand"),(8,15,"desc"),(16,20,"desc"),(21,32,"product")]}),
("kate somerville exfolikate intensive exfoliating treatment",{"entities":[(0,15,"brand"),(16,26,"desc"),(27,36,"desc"),(37,48,"desc"),(49,58,"product")]}),
("kiehl's creamy eye treatment with avocado",{"entities":[(0,7,"brand"),(8,14,"desc"),(15,18,"desc"),(19,28,"product"),(34,41,"desc")]}),
("kiku masamune high moist lotion",{"entities":[(0,13,"brand"),(14,18,"desc"),(19,24,"desc"),(25,31,"product")]}),
("korres greek yoghurt nourishing probiotic gel cream moisturizer",{"entities":[(0,6,"brand"),(7,12,"desc"),(13,21,"desc"),(21,32,"desc"),(32,41,"desc"),(42,45,"product"),(46,51,"product"),(52,63,"product")]}),
("la roche posay toleriane hydrating gentle facial cleanser ",{"entities":[(0,14,"brand"),(15,24,"desc"),(25,34,"desc"),(35,41,"desc"),(42,48,"desc"),(49,58,"product")]}),
("lush ultrabland",{"entities":[(0,4,"brand"),(5,15,"desc")]}),
("makeup artist's choice 15% mandelic acid & 15% salisylic acid",{"entities":[(0,22,"brand"),(27,36,"desc"),(36,41,"desc"),(47,57,"desc"),(57,61,"desc")]}),
("mizon snail recovery gel cream",{"entities":[(0,5,"brand"),(6,11,"desc"),(12,20,"desc"),(21,24,"product"),(25,30,"product")]}),
("muji sensitive skin moisturizing milk, high moisture",{"entities":[(0,4,"brand"),(5,14,"desc"),(15,20,"desc"),(20,33,"desc"),(33,37,"product"),(39,44,"desc"),(44,52,"desc")]}),
("neutrogena hydro boost gel cream with hyaluronic acid for extra dry skin",{"entities":[(0,10,"brand"),(11,16,"desc"),(17,22,"desc"),(23,26,"product"),(27,32,"product"),(38,48,"desc"),(49,53,"desc"),(58,63,"desc"),(64,67,"desc"),(68,72,"desc")]}),
#60
("neutrogena hydro boost water gel",{"entities":[(0,10,"brand"),(11,16,"desc"),(17,22,"desc"),(23,28,"desc"),(29,32,"product")]}),
("niod low viscosity cleaning ester",{"entities":[(0,4,"brand"),(5,8,"desc"),(9,18,"desc"),(19,27,"desc"),(28,33,"product")]}),
("nivea moisture care",{"entities":[(0,5,"brand"),(6,14,"desc"),(15,19,"desc")]}),
("nivea sun care uv milky gel spf 50+ pa++++ ",{"entities":[(0,5,"brand"),(6,9,"desc"),(10,14,"desc"),(15,17,"desc"),(18,23,"desc"),(24,27,"product"),(28,31,"desc")]}),
("now solutions pure lanolin",{"entities":[(0,13,"brand"),(14,18,"desc"),(19,26,"desc")]}),
("nufountain c20 + ferulic vitamin c",{"entities":[(0,10,"brand"),(17,24,"desc"),(25,34,"desc")]}),
("ocusoft foaming lid scrub",{"entities":[(0,7,"brand"),(8,15,"desc"),(16,19,"desc"),(20,25,"product")]}),
("paula's choice 2% bha body spot exfoliant",{"entities":[(0,14,"brand"),(15,17,"desc"),(18,21,"desc"),(27,31,"desc"),(32,41,"product")]}),
("paula's choice skin perfecting 2% bha liquid exfoliant",{"entities":[(0,14,"brand"),(15,20,"desc"),(20,30,"desc"),(34,36,"desc"),(34,38,"desc"),(38,45,"desc"),(45,54,"product")]}),
("ren evercalm gentle cleansing milk",{"entities":[(0,3,"brand"),(4,12,"desc"),(13,19,"desc"),(20,29,"desc"),(30,34,"product")]}),
#70
("rhoto skin aqua uv super moisture gel spf 50+ pa++++",{"entities":[(0,5,"brand"),(6,10,"desc"),(11,15,"desc"),(16,18,"desc"),(19,23,"desc"),(19,24,"desc"),(25,32,"desc"),(25,33,"desc"),(34,37,"product"),(38,40,"desc"),(38,41,"desc")]}),
("roc retinol correxion eye cream",{"entities":[(0,3,"brand"),(4,11,"desc"),(12,21,"desc"),(22,25,"desc"),(26,31,"product")]}),
("scinic honey all in one ampoule",{"entities":[(0,6,"brand"),(7,12,"desc"),(13,23,"desc"),(24,31,"product")]}),
("simple refreshing facial wash",{"entities":[(0,6,"brand"),(7,17,"desc"),(18,24,"desc"),(25,29,"product")]}),
("skinceuticals physical fusion uv defense spf 50",{"entities":[(0,13,"brand"),(14,22,"desc"),(23,29,"desc"),(30,32,"desc"),(33,40,"desc"),(41,44,"desc")]}),
("st ives timeless skin collagen elastin facial moisturizer",{"entities":[(0,7,"brand"),(8,16,"desc"),(17,21,"desc"),(22,30,"desc"),(31,38,"desc"),(39,45,"desc"),(46,57,"product")]}),
("stratia velvet cleansing milk",{"entities":[(0,7,"brand"),(8,14,"desc"),(15,24,"desc"),(25,29,"product")]}),
("stridex maximum strength pads",{"entities":[(0,7,"brand"),(8,15,"desc"),(16,24,"desc"),(25,29,"product")]}),
("sunday riley good genes",{"entities":[(0,12,"brand"),(13,23,"desc")]}),
("supergoop play everyday lotion spf 50 with sunflower extract",{"entities":[(0,9,"brand"),(10,15,"desc"),(15,24,"desc"),(24,31,"product"),(31,35,"desc"),(43,53,"desc"),(53,60,"desc")]}),
("thalgo eveil la mer gentle cleansing milk ",{"entities":[(0,19,"brand"),(20,26,"desc"),(27,36,"desc"),(37,42,"product")]}),
("the body shop body butter",{"entities":[(0,13,"brand"),(19,25,"product")]}),
("the jojoba company jojoba oil",{"entities":[(0,18,"brand"),(19,26,"desc"),(26,29,"product")]}),
("the ordinary 100% l ascorbic acid powder, mixed with the ordinary resveratrol 3% ferulic acid 3% vitamin c ",{"entities":[(0,12,"brand"),(20,28,"desc"),(29,34,"desc"),(34,40,"product"),(54,65,"brand"),(66,78,"desc"),(81,89,"desc"),(89,94,"desc"),(97,107,"desc")]}),
("the ordinary glycolic acid 7% toning solution",{"entities":[(0,12,"brand"),(13,21,"desc"),(22,27,"desc"),(30,37,"desc"),(37,45,"product")]}),
("the ordinary natural moisturizing factors + ha",{"entities":[(0,12,"brand"),(13,20,"desc"),(21,33,"desc"),(34,41,"desc"),(44,46,"desc")]})]

for text, annot in tqdm(TRAIN_DATA):
    doc = nlp.make_doc(text)
    ents = []
    for start, end, label in annot["entities"]:
        span = doc.char_span(start, end, label=label, alignment_mode="contract")
        if span is None:
            print("Skipping entity")
        else:
            ents.append(span)
    doc.ents = ents 
    db.add(doc)

db.to_disk("./train.spacy")