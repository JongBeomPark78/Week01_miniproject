from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.wd6li.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

doc = {
    'image':'https://w.namu.la/s/4d772908e1563861ba6faa7194ca8035a4462f4865326c3c010d683a4237ed1aaab87f3812a18b43c359b5ea83003b0bc8145bcf367e1e7863c3576df37df8d0d00c15dd7fa8abc81275a25c300562a085849a2c032a563aba5a870d6088ad2af33de0f6d4d79201b7c25bba4c3a5431',
    'Name' : '김승규',
    'Position' : 'GK',
    'Team' : '알 샤바르 FC',
    'Link' : 'https://namu.wiki/w/%EA%B9%80%EC%8A%B9%EA%B7%9C',
    'Card_number' : 1,
    'Like_Count' : 0

}
db.player.insert_one(doc)

doc = {
    'image':'https://w.namu.la/s/71a40e18c803967157a0e255dcebc22b968d7eca37dd2cc9a80f3710365b050f779332afddbc229834a618154caaae5a8f00ffbc74a9beacfc1451ca9e83a99665e43301a7b87920667287e89e5b88c38ae93bceef7dfbe8bf8364bb847868e764c5bb162ade58dc63ea40378e315002',
    'Name' : '조현우',
    'Position' : 'GK',
    'Team' : '울산 현대',
    'Link' : 'https://namu.wiki/w/%EC%A1%B0%ED%98%84%EC%9A%B0',
    'Card_number' : 2,
    'Like_Count' : 0

}
db.player.insert_one(doc)

doc = {
    'image':'https://w.namu.la/s/897e259fa4431b09428b523c926b89bbfa9c5907fafe279bbe249084eb9ab1f3b418f0a329241c0164b6a47ee6eabbeaa05f92bbdee3452dbbb56fcc0cd2abf97214d9b86ea57801e7394288401279b8488a03f7aae0b1334294ae5e352487488da2f2c47e9e3b3cfc2fd07c6509e387',
    'Name' : '송범근',
    'Position' : 'GK',
    'Team' : '전북 현대 모터스',
    'Link' : 'https://namu.wiki/w/%EC%86%A1%EB%B2%94%EA%B7%BC',
    'Card_number' : 3,
    'Like_Count': 0
}
db.player.insert_one(doc)

doc = {
    'image':'https://w.namu.la/s/2c5f21b45ee2c639a3b422e195587aa38b180718448e51589fd2ebfb95e63fd51aed29b48035acfe9f8367f61aea616cd7b697cc0c512eafe327ba779408155cd7821f3fe35fcb93517d7690b80cb5d2fc199cc5b7eae630a9702b85ab6bc437',
    'Name' : '김민재',
    'Position' : 'DF',
    'Team' : 'SSC 나폴리',
    'Link' : 'https://namu.wiki/w/%EA%B9%80%EB%AF%BC%EC%9E%AC',
    'Card_number' : 4,
    'Like_Count': 0
}
db.player.insert_one(doc)

doc = {
    'image':'https://w.namu.la/s/7abf851b402a389433e88f563f44e3e5f42fd7c5323d70663554d980160aba246c5f7ede301d68c434876c201819179fa86c61e7f45221b2560cf2f94c3222acc83e85882f9784b863214075984c6f065e733ad471aac743635638b2050f082c9e79c166dc6fbc36f6154c1bca9a6062',
    'Name' : '김영권',
    'Position' : 'DF',
    'Team' : '울산 현대',
    'Link' : 'https://namu.wiki/w/%EA%B9%80%EC%98%81%EA%B6%8C',
    'Card_number' : 5,
    'Like_Count': 0
}
db.player.insert_one(doc)

doc = {
    'image':'https://w.namu.la/s/30e45bda9388137574c53c541d8cb326e467bb311135ce72d4cd38ce3eb3bee74dccb766f35232863f3f5d3714301daadfd0825e39e52c3dcb682791188123b8eef2d7b0e11684138eb8c0d55a2174b675d8cd23a049e227f1762f78ce7ab7c31caa50cd1c0ddbd0a2ef3741a84fa859',
    'Name' : '권경원',
    'Position' : 'DF',
    'Team' : '감바 오사카',
    'Link' : 'https://namu.wiki/w/%EA%B6%8C%EA%B2%BD%EC%9B%90',
    'Card_number' : 6,
    'Like_Count': 0
}
db.player.insert_one(doc)

doc = {
    'image':'https://img.sbs.co.kr/newsnet/etv/upload/2022/01/18/30000737582_500.jpg',
    'Name' : '조유민',
    'Position' : 'DF',
    'Team' : '대전 하나 시티즌',
    'Link' : 'https://namu.wiki/w/%EC%A1%B0%EC%9C%A0%EB%AF%BC',
    'Card_number' : 7,
    'Like_Count': 0
}
db.player.insert_one(doc)

doc = {
    'image':'https://w.namu.la/s/3045721384c5d7ae31200799e7b15920260a93bcb88188ed2e219455668a2ddfa70af8115867b3a2a0520ce6a05d7279296f3b19bc6155140691774989c7f7070936ec7083bddbc1fdcaa0b432e3e861dddb9bc15a3add25aa33cf5791e9376c',
    'Name' : '김문환',
    'Position' : 'DF',
    'Team' : '전북 현대 모터스',
    'Link' : 'https://namu.wiki/w/%EA%B9%80%EB%AC%B8%ED%99%98',
    'Card_number' : 8,
    'Like_Count': 0
}
db.player.insert_one(doc)

doc = {
    'image':'https://w.namu.la/s/ded7de5deffad2a4bccef30874bee44800b2329d46aa8b31feb7935f4f7e116239c355178053ab8be4e5694d071f8fdee94ca2d634949f28fd30168011c0177db21d52b0fc59ae58171a3a57668e2833f212858ec330d25a7d71c9c56fc580d758fff1b5f2cab334202269d97b14bf72',
    'Name' : '윤종규',
    'Position' : 'DF',
    'Team' : 'FC 서울',
    'Link' : 'https://namu.wiki/w/%EC%9C%A4%EC%A2%85%EA%B7%9C(%EC%B6%95%EA%B5%AC%EC%84%A0%EC%88%98)',
    'Card_number' : 9,
    'Like_Count': 0
}
db.player.insert_one(doc)

doc = {
    'image':'https://w.namu.la/s/a2641c2633c0046eb999d695b9696e0e94f02f088a0a4774fb52002fe26e1b75559a43397ecde743277f976720338f0c891bf5bd079e827e9673e5e1dfd6ce07724109fe00564c20bd383b3d346204677be69b8971264c2113d1d5c0ecd82a4afafa00842d47e8bd1327ac60463b8b4b',
    'Name' : '김태환',
    'Position' : 'DF',
    'Team' : '울산 현대',
    'Link' : 'https://namu.wiki/w/%EA%B9%80%ED%83%9C%ED%99%98(1989)',
    'Card_number' : 10,
    'Like_Count': 0
}
db.player.insert_one(doc)

doc = {
    'image':'https://w.namu.la/s/cb70b62e3d5651d121f321c01214d7acb5b5800f4e7f3f02d2f64410e15a00b896ec10d920cdd8e8111536d35a2ba357734e98edf8145ea7f89b751444f8cf7f8158b6db0fb2dd5d8e8fb470fa4384452bd74beac8e874070b5edd7bea0f3a8331ee10f940ada30b2bf92d03e6f94bca',
    'Name' : '김진수',
    'Position' : 'DF',
    'Team' : '전북 현대 모터스',
    'Link' : 'https://namu.wiki/w/%EA%B9%80%EC%A7%84%EC%88%98(%EC%B6%95%EA%B5%AC%EC%84%A0%EC%88%98)',
    'Card_number' : 11,
    'Like_Count': 0
}
db.player.insert_one(doc)

doc = {
    'image':'https://w.namu.la/s/1344eab442f99adae4cee554e1defe3a45b9d5f9960e069dec845241d09cd95c9b5a1b9a49bceb3f5befba5e05dcb2548bd8ef195b0a7bb19f89a3030571a323f98e7a8e7b4857121d8c432cf5e0f8e364448d9f69ef4fbae2ed42f690268324',
    'Name' : '홍철',
    'Position' : 'DF',
    'Team' : '대구 FC',
    'Link' : 'https://namu.wiki/w/%ED%99%8D%EC%B2%A0',
    'Card_number' : 12,
    'Like_Count': 0
}
db.player.insert_one(doc)

doc = {
    'image':'https://w.namu.la/s/76b56a368b11d2f8d0037637e8ae5d6935f12c65330464116c70e6f0927d440188a6c1b0cc5ba8c91bbc86fcca3093ad3121b65b4f261be40b0ec9f6f4cce763a6df439e2bfddf005705e007fc840b7a850e7dedf5d74cffd30c28be57b5bfd569d8dbfefe787792fc82ad81f8a8fbfb',
    'Name' : '정우영',
    'Position' : 'MF',
    'Team' : '알 사드 SC',
    'Link' : 'https://namu.wiki/w/%EC%A0%95%EC%9A%B0%EC%98%81(1989)',
    'Card_number' : 13,
    'Like_Count': 0
}
db.player.insert_one(doc)

doc = {
    'image':'https://cdn.gukjenews.com/news/photo/202207/2506878_2506128_3815.jpg',
    'Name' : '손준호',
    'Position' : 'MF',
    'Team' : '산둥 타이산',
    'Link' : 'https://namu.wiki/w/%EC%86%90%EC%A4%80%ED%98%B8(%EC%B6%95%EA%B5%AC%EC%84%A0%EC%88%98)',
    'Card_number' : 14,
    'Like_Count': 0
}
db.player.insert_one(doc)

doc = {
    'image':'https://w.namu.la/s/8ee209b79934fc61f915669467eaf29ee11922f283ba97b6328724556f02478bfcd13b9ea4d5f656c35b3af459791ae72b2a7d013d3b17df12ce892411a464e68547a08507f2bd5681d9e4bf35cb71a693ed8377e23ffcbf4bba8e52995636e7a025189ebd38e7752ba98b496e16f5e4',
    'Name' : '백승호',
    'Position' : 'MF',
    'Team' : '전북 현대 모터스',
    'Link' : 'https://namu.wiki/w/%EB%B0%B1%EC%8A%B9%ED%98%B8',
    'Card_number' : 15,
    'Like_Count': 0
}
db.player.insert_one(doc)

doc = {
    'image':'https://w.namu.la/s/0a3163f6ec589817066951e71ff67d89bf1d513a51d9446dffc4314013911dad3367f916588d7c0f7d395da4972626e2e0ad32d14c69416a869adb271df03c27fb9277d7b509fa19a7275279bf448248e96d7e6ebd1622f20e6a887006a7c3e1',
    'Name' : '황인범',
    'Position' : 'MF',
    'Team' : '올림피아코스 FC',
    'Link' : 'https://namu.wiki/w/%ED%99%A9%EC%9D%B8%EB%B2%94',
    'Card_number' : 16,
    'Like_Count': 0
}
db.player.insert_one(doc)

doc = {
    'image':'https://w.namu.la/s/1677142baa63e00661f36ea3de3eeba0f85748e7777559cb7672ea91895240445de2d55921d64a97274b11773deb00834fc8bf0f6c0d0f17ab113acbee5dea70fe03f6d066e62f48432fb91120e4169c4151db32ce9b39dab27ce711e5a137a2',
    'Name' : '이재성',
    'Position' : 'MF',
    'Team' : 'FSV 마인츠 05',
    'Link' : 'https://namu.wiki/w/%EC%9D%B4%EC%9E%AC%EC%84%B1',
    'Card_number' : 17,
    'Like_Count': 0
}
db.player.insert_one(doc)

doc = {
    'image':'https://w.namu.la/s/6fa2bcce9f345e805d09f032aadac9ec7d9a16d7c5a6a31d2a8dd7be0ffa769ac5f6ca3c780fddc7ebb8029677491f2c9bf9ee9f53e19b897031e22fedb5eb13e56e3eb70fc398c59ac39f75ec2f7e9c97e5a47d40f9da0b9a456f083f3f9866',
    'Name' : '권창훈',
    'Position' : 'MF',
    'Team' : '김천 상무 FC',
    'Link' : 'https://namu.wiki/w/%EA%B6%8C%EC%B0%BD%ED%9B%88',
    'Card_number' : 18,
    'Like_Count': 0
}
db.player.insert_one(doc)

doc = {
    'image':'https://w.namu.la/s/089ac91dede31a2b624f5236cbc27188d8235a1436c16b8aa117fb86fd766183377651bf29444f79c89b323024939502a5f10f887faf16e3be4ddd1485904a41bb97531ce4d3768eea57f9882f51e65a3a2ef9b7cdcb0eafa8a17955e64df17a',
    'Name' : '정우영',
    'Position' : 'MF',
    'Team' : 'SC 프라이부르크',
    'Link' : 'https://namu.wiki/w/%EC%A0%95%EC%9A%B0%EC%98%81(1999%EB%85%84%EC%83%9D%20%EC%B6%95%EA%B5%AC%EC%84%A0%EC%88%98)',
    'Card_number' : 19,
    'Like_Count': 0
}
db.player.insert_one(doc)

doc = {
    'image':'https://w.namu.la/s/206b9c3c7171ee985c9151102c884b679ca64876d63b5210c967bbe95fa5ceef58b963177a75a48e2c4b4d4bc4a08733aaa059609370b00bb02875d70db9e99a281a5a58177e0d7a1abf269473883c15434df5b7ac704947f685b82cc6b507ad3094c9493fd1187a499069d7039e54fd',
    'Name' : '이강인',
    'Position' : 'MF',
    'Team' : 'RCD 마요르카',
    'Link' : 'https://namu.wiki/w/%EC%9D%B4%EA%B0%95%EC%9D%B8',
    'Card_number' : 20,
    'Like_Count': 0
}
db.player.insert_one(doc)

doc = {
    'image':'https://w.namu.la/s/1a40140b91e2ff9631c429e3968ffa65dc8a7ef1f40518c1c9ae814d973443eee4c339f5798b7bba3f422ec3bb9c6a71cfb42f7d116c16ee540ca0f57ae2fd6537d39736d0a051ad554e7b723f8ee0c33b5adf5efd0327cb635cea26c844c9f2',
    'Name' : '손흥민',
    'Position' : 'MF',
    'Team' : '토트넘 홋스퍼 FC',
    'Link' : 'https://namu.wiki/w/%EC%86%90%ED%9D%A5%EB%AF%BC',
    'Card_number' : 21,
    'Like_Count': 0
}
db.player.insert_one(doc)

doc = {
    'image':'https://w.namu.la/s/58eedc31aacdd0d1acd3c01683a27264a02ae5448bfcba8ad05d5b1989047a599cc73d815f9a54789d820e2fb0d0c8ba7fa6c96792741c71a753798b41ceff60fa2398dcea6321181129d9bd550cd4b1f3285cd23adc4458b7dc56cd37addfa7',
    'Name' : '황희찬',
    'Position' : 'MF',
    'Team' : '울버햄튼 원더러스 FC',
    'Link' : 'https://namu.wiki/w/%ED%99%A9%ED%9D%AC%EC%B0%AC',
    'Card_number' : 22,
    'Like_Count': 0
}
db.player.insert_one(doc)

doc = {
    'image':'https://w.namu.la/s/0de6745d26f128c04d2e98f0a031e016462b297189226ec05e2d555c2a4bdfbc7b4ec758dff98e598fd723de938f91c4af186bd7354156be56f9f10b1d4b09e5de89d94a692dfb3360b236ce6f5c0b29fbcd6ba051f69a8b35e88b289abe2aab5444385301e77491ca73c0596469bd54',
    'Name' : '나상호',
    'Position' : 'MF',
    'Team' : 'FC 서울',
    'Link' : 'https://namu.wiki/w/%EB%82%98%EC%83%81%ED%98%B8',
    'Card_number' : 23,
    'Like_Count': 0
}
db.player.insert_one(doc)

doc = {
    'image':'https://w.namu.la/s/9f24d272520ff05fb6d71ce8fbe8a173880d446a39efd69d066db7435c91e47913cd558f9230a75ef6c2e599801faf0e02a1e2f2399c05786232de5eb95babfa460414def60da8f5f3f504d2485de3173dc75d23f5fdf5d6003c321913d479ad3b4000ae4f0643562e9e1631a51298a2',
    'Name' : '송민규',
    'Position' : 'MF',
    'Team' : '전북 현대 모터스',
    'Link' : 'https://namu.wiki/w/%EC%86%A1%EB%AF%BC%EA%B7%9C',
    'Card_number' : 24,
    'Like_Count': 0
}
db.player.insert_one(doc)

doc = {
    'image':'https://w.namu.la/s/f0155eeadc379e3dfc6c68ef734790327c4c96474789420d067487c2986d386caa906a605975d256f92c8ac5d90bac6c793420e1d8919f482a4bac2d36a0f3b8f388a38010c5fd1510fb9bbdb1ca517e7f498c16e535e9d7fb91a550212248bd',
    'Name' : '황의조',
    'Position' : 'MF',
    'Team' : '올림피아코스 FC',
    'Link' : 'https://namu.wiki/w/%ED%99%A9%EC%9D%98%EC%A1%B0',
    'Card_number' : 25,
    'Like_Count': 0
}
db.player.insert_one(doc)

doc = {
    'image':'https://post-phinf.pstatic.net/MjAyMDA1MjVfMjc5/MDAxNTkwMzQwMTM0MDkz.hSALQqHn3TCjAPtrCBJ3XwYIJIU20RmLFlSW88z4WRsg.YiTPQyTad26_dsouh5pG_5Ll5Qb1JuIm8MFm4SJULCEg.PNG/image.png?type=w1200',
    'Name' : '조규성',
    'Position' : 'FW',
    'Team' : '전북 현대 모터스',
    'Link' : 'https://namu.wiki/w/%EC%A1%B0%EA%B7%9C%EC%84%B1',
    'Card_number' : 26,
    'Like_Count': 0
}
db.player.insert_one(doc)


