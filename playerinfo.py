from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.wd6li.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

doc = {
    'image':'https://w.namu.la/s/59d12c429b57370b667f3d77a73a426786f560fd99c4fb08cdaa92765e8d97b62428879c4e80e452979aec7acadd6dd619bf688f59d78b5dcb2ac9df40b52217684d01e57c0ee37041fe6ce8d435bb3031d711f177dcb3bfc48886ba3e06804a6a4fdcb8affbd1dd007ab79075ad427d',
    'Name' : '김승규',
    'Position' : 'GK',
    'Team' : '알 샤바르 FC',
    'Link' : 'https://namu.wiki/w/%EA%B9%80%EC%8A%B9%EA%B7%9C',
    'Card_number' : 1,
    'Like_Count' : 0

}
db.player.insert_one(doc)

doc = {
    'image':'https://w.namu.la/s/95ee2ce86d7e481eeb4a34d58f91da1dc3dcae6fcab00752b4d43b43885ace82feca6313fb2a6ac7cdc152fcd74607933f2721d8af516a90f1460cc1d957aafaa32c4d90cbcdb412c8cf94737cd1254e8187291abb2c10dcbcadd89429de6c01c9cf97d5ab46d668daf5f01f5d91d42c',
    'Name' : '조현우',
    'Position' : 'GK',
    'Team' : '울산 현대',
    'Link' : 'https://namu.wiki/w/%EC%A1%B0%ED%98%84%EC%9A%B0',
    'Card_number' : 2,
    'Like_Count' : 0

}
db.player.insert_one(doc)

doc = {
    'image':'https://w.namu.la/s/a48af662dab26f13eb84214279bdc523fb1d970547b9159c82e9da99652474aae1404b057d1f1bebcb3cee41fd912dffe2a37ceec11ab87fd3aa879f3b2c17055e152a6340826a3c6cbc1c6283e81d9427b394c99f93f7c398ce55f1c9583a4c61d55ebbbee82f806dd1623085f89439',
    'Name' : '송범근',
    'Position' : 'GK',
    'Team' : '전북 현대 모터스',
    'Link' : 'https://namu.wiki/w/%EC%86%A1%EB%B2%94%EA%B7%BC',
    'Card_number' : 3,
    'Like_Count': 0
}
db.player.insert_one(doc)

doc = {
    'image':'https://w.namu.la/s/a168f8ccb340f051df836e5aeb9a83f49881b8b1466ff821310603ea68e90d408823206ffa0b7aafa4eb72cc09431f0b9371fc85d376bde081b77d22e54d779d6185f3cfdd452fa6bcb13d71603b6c317607a82ad49b0ebd68ee9e87818484b26059c2393845d8ab239b7dbef2b80a49',
    'Name' : '김민재',
    'Position' : 'DF',
    'Team' : 'SSC 나폴리',
    'Link' : 'https://namu.wiki/w/%EA%B9%80%EB%AF%BC%EC%9E%AC',
    'Card_number' : 4,
    'Like_Count': 0
}
db.player.insert_one(doc)

doc = {
    'image':'https://w.namu.la/s/a73006f0d3d2a9685efddc36f975570e2c7a64eea8c773253b970878b9dfaa326aea0e6918ca04bbec842a0ff87da66c106b8b0956083f6c66f9d4c7e2a6bb9c3306e8022b4bad5e90c8eb64123b5143090ec6491cb5ef5357e963cc2ae85c0e1db8f4a41d48e0b83418242d025a24d3',
    'Name' : '김영권',
    'Position' : 'DF',
    'Team' : '울산 현대',
    'Link' : 'https://namu.wiki/w/%EA%B9%80%EC%98%81%EA%B6%8C',
    'Card_number' : 5,
    'Like_Count': 0
}
db.player.insert_one(doc)

doc = {
    'image':'https://w.namu.la/s/a35c13ea1b2d8905a47a551787f8196094137c2e10fd2355ece8f5e01b99b3d029d6c2b3d019cd5914ef54f6eacd39949dccba82e4eddd65fe824fca7890d9aa48c1e601165079f03be25d7dc7a8b6a8e0846d0f018abb269f008bc4e85cf5669c724b9a0a42ceeec7cb8acb8c471510',
    'Name' : '권경원',
    'Position' : 'DF',
    'Team' : '감바 오사카',
    'Link' : 'https://namu.wiki/w/%EA%B6%8C%EA%B2%BD%EC%9B%90',
    'Card_number' : 6,
    'Like_Count': 0
}
db.player.insert_one(doc)

doc = {
    'image':'https://w.namu.la/s/b3abbec223a4398f820af1d1ed0c31c1822a86f7547e2d1929b11e8757968617314e8628c2eb3f9f095590435d0b652ad22e74497e03fc48025496505fd8450ce5de8ed126c2b005dedd434d7d77d1ae7acce0b8862e3cd7ca022209c6d9f896810f9109bed2fcf277ed74ff56b696a9',
    'Name' : '조유민',
    'Position' : 'DF',
    'Team' : '대전 하나 시티즌',
    'Link' : 'https://namu.wiki/w/%EC%A1%B0%EC%9C%A0%EB%AF%BC',
    'Card_number' : 7,
    'Like_Count': 0
}
db.player.insert_one(doc)

doc = {
    'image':'https://w.namu.la/s/2c6381e1ea6c564bec3f782a28e4ed4ae23af49d13ee86acc130eec0ba5996ce6d7cb6b99858e7d410aacd71684a916c32498ce85e9c1ec80c3eac45c25e824c1c1756f30f2c65a90614f20f6fdc0f4fdbed1618eb3e50933e59f19a18d6bfb2c8e7199195b60782988e971d36dfa651',
    'Name' : '김문환',
    'Position' : 'DF',
    'Team' : '전북 현대 모터스',
    'Link' : 'https://namu.wiki/w/%EA%B9%80%EB%AC%B8%ED%99%98',
    'Card_number' : 8,
    'Like_Count': 0
}
db.player.insert_one(doc)

doc = {
    'image':'https://w.namu.la/s/2a979df2022a5a6f3f2ea791d86a2802477732ee8cbf0ca877b795cd5c571353a1efb25a19d8693f420b32ed7b4e72712729528d64c63059e238780ec9439c111c9a373ed9c8b24e7280d7179a6b96ea3fc3af9061421a69a7df524754fcc8f4d3cc5b0ba87a56ebe058a1cd99c0ea24',
    'Name' : '윤종규',
    'Position' : 'DF',
    'Team' : 'FC 서울',
    'Link' : 'https://namu.wiki/w/%EC%9C%A4%EC%A2%85%EA%B7%9C(%EC%B6%95%EA%B5%AC%EC%84%A0%EC%88%98)',
    'Card_number' : 9,
    'Like_Count': 0
}
db.player.insert_one(doc)

doc = {
    'image':'https://w.namu.la/s/2cc25f0550f22f1101d2a4fbeb12e23e86357452adc4849195d47b31799b86123e8792a171aa2902836ad742cc2aca398a8dc00cafb58e2614d19ba89388b2a539de4faf073d52d1c747590d3a6c97825bb6fdd6c2b577eec4bc767c03f78fe52ed1a9400eacbaa449a26424b28cc882',
    'Name' : '김태환',
    'Position' : 'DF',
    'Team' : '울산 현대',
    'Link' : 'https://namu.wiki/w/%EA%B9%80%ED%83%9C%ED%99%98(1989)',
    'Card_number' : 10,
    'Like_Count': 0
}
db.player.insert_one(doc)

doc = {
    'image':'https://w.namu.la/s/bf9515cfcdaa27e153b5359f3162331dd592e0556623416056a8bf4645c8f62d1e1501a28a36860077571fac33a3d5d1a9d991ac1795f0361ed29c61eaeb21811d19226e9796b8d85e63504496978690473ad682ad04b58bd109fff3b9f96b22a887e915f2a05638d40727994334613f',
    'Name' : '김진수',
    'Position' : 'DF',
    'Team' : '전북 현대 모터스',
    'Link' : 'https://namu.wiki/w/%EA%B9%80%EC%A7%84%EC%88%98(%EC%B6%95%EA%B5%AC%EC%84%A0%EC%88%98)',
    'Card_number' : 11,
    'Like_Count': 0
}
db.player.insert_one(doc)

doc = {
    'image':'https://w.namu.la/s/e676abc4db063914b878685fb519485fe22904e7685542bf22be8412e370743f8defde43b641eff4416fc54fb92ee67f554e03739a13298e26d11e4d5771803410a9f869721f484f6adaec3ed2903a242eac8f1ca7f97fa3ae3cf7c2671ca2508de9b1572da05f3b100f6ce2010d6b73',
    'Name' : '홍철',
    'Position' : 'DF',
    'Team' : '대구 FC',
    'Link' : 'https://namu.wiki/w/%ED%99%8D%EC%B2%A0',
    'Card_number' : 12,
    'Like_Count': 0
}
db.player.insert_one(doc)

doc = {
    'image':'https://w.namu.la/s/298aa94c09bd5808938cf2bb9e35dbe6e6441956be471319e1e101fd61b4ad9087d41cb91cdf139b4e251333a04b1e873d63ebb4383fa7afc3180dc60f245c767b67e1dd35517b9ba0917073f7f91a3a8396f89ee34e58851f5ac9c078a6f5bbe01cef9a45903de58cb15d131a4c4676',
    'Name' : '정우영',
    'Position' : 'MF',
    'Team' : '알 사드 SC',
    'Link' : 'https://namu.wiki/w/%EC%A0%95%EC%9A%B0%EC%98%81(1989)',
    'Card_number' : 13,
    'Like_Count': 0
}
db.player.insert_one(doc)

doc = {
    'image':'https://w.namu.la/s/a249471816cbe13a85e3bc99e6e25a2f33be0a72ea990d8ea57fa0384f4a31c00206ee88f1f710651ecd0859f566947b7eedf23d34da7e163b212a698af709e745b2661bda9df0f6fe207017fb3f32bf1033fd03732430c7d8cfe514cafe1826c3093646d46b4656daaf29e733444f56',
    'Name' : '손준호',
    'Position' : 'MF',
    'Team' : '산둥 타이산',
    'Link' : 'https://namu.wiki/w/%EC%86%90%EC%A4%80%ED%98%B8(%EC%B6%95%EA%B5%AC%EC%84%A0%EC%88%98)',
    'Card_number' : 14,
    'Like_Count': 0
}
db.player.insert_one(doc)

doc = {
    'image':'https://w.namu.la/s/b5c11496d38e456f2ab7766c32650112597a592ba16f0881aef0f2a638caf63f6a190022115c1be61aa4f8e3bd2af3ee6b54370ca28c52b02650aff431bd18f3d6171b0dc1c3a1d72b3145923022ee3f842eb0aacc201a123439a4325b2a4c52a78c508e3e3f5694c74337a878ee5a29',
    'Name' : '백승호',
    'Position' : 'MF',
    'Team' : '전북 현대 모터스',
    'Link' : 'https://namu.wiki/w/%EB%B0%B1%EC%8A%B9%ED%98%B8',
    'Card_number' : 15,
    'Like_Count': 0
}
db.player.insert_one(doc)

doc = {
    'image':'https://w.namu.la/s/169332f8165e7e12516fff32000bf80a896f7b7a4549dfb60434ea32f568fefe4b2e00f6ac7baa39dd3972cd0e57cd134f66b54e627857921cc89f799a5733743c8ced9e0b2480f729e5d0af11c953e94638e2377e93aef5c49913a7e991eff398e59785699a2e1e1f2855220981e799',
    'Name' : '황인범',
    'Position' : 'MF',
    'Team' : '올림피아코스 FC',
    'Link' : 'https://namu.wiki/w/%ED%99%A9%EC%9D%B8%EB%B2%94',
    'Card_number' : 16,
    'Like_Count': 0
}
db.player.insert_one(doc)

doc = {
    'image':'https://w.namu.la/s/77166bd9e274d3cb844779afe3fac44f94858eac07d0c3168bc4a87f9b779982a18ba8902291e1900537eae2739702d1e1b1ce96e299a358b19c14a719be29a625b9e23fea26851d38763fdfa44fbb29f4f5379cd747a4bfe3898c705710b036fd9b277c5a22dee4cdd4ca6bbca12476',
    'Name' : '이재성',
    'Position' : 'MF',
    'Team' : 'FSV 마인츠 05',
    'Link' : 'https://namu.wiki/w/%EC%9D%B4%EC%9E%AC%EC%84%B1',
    'Card_number' : 17,
    'Like_Count': 0
}
db.player.insert_one(doc)

doc = {
    'image':'https://w.namu.la/s/57744a954768d2f00e88cdef999e2e211460b1bd5d5f2bd37e29878aefe6dee6ada32ba18f972fafab82cbe1f6327f966bc168b2b7adae2e5453218b62a938f78bf3f1baa24ceac265bdc011a3b68f8098ef90cfd44cab1cf80f746cb07f1698dd0019f2c3c2e42ca2cb9e9cb3edd21b',
    'Name' : '권창훈',
    'Position' : 'MF',
    'Team' : '김천 상무 FC',
    'Link' : 'https://namu.wiki/w/%EA%B6%8C%EC%B0%BD%ED%9B%88',
    'Card_number' : 18,
    'Like_Count': 0
}
db.player.insert_one(doc)

doc = {
    'image':'https://w.namu.la/s/c461404117b746b728679e976cd79ae9b18af385018396f6814327cd6b49a300e0ffbbc58612dc380bce97991ef2ee52059891ec20c1d915610d1c77fdcf7fb5bc6e4fa88bdd2bcd7c2f1ca215c764f32f64458c564c7e82b550ceb41658f4dfe995b769a60b884b511da49c2a8a8ec4',
    'Name' : '정우영',
    'Position' : 'MF',
    'Team' : 'SC 프라이부르크',
    'Link' : 'https://namu.wiki/w/%EC%A0%95%EC%9A%B0%EC%98%81(1999%EB%85%84%EC%83%9D%20%EC%B6%95%EA%B5%AC%EC%84%A0%EC%88%98)',
    'Card_number' : 19,
    'Like_Count': 0
}
db.player.insert_one(doc)

doc = {
    'image':'https://w.namu.la/s/9222493cd206b2751894f5e687860d6eab716385564118f98d2c8e34a200eec24fa9fcc2e3855918ef63e3a0bf9e6833d6257b15532482f63f32c920252b82dc29a8ab11bbfa4f5e818fc41e896ac83e351859da09f793d921eb6d6eb555a399bcd34b7731c5566128c38d25fa32e07c',
    'Name' : '이강인',
    'Position' : 'MF',
    'Team' : 'RCD 마요르카',
    'Link' : 'https://namu.wiki/w/%EC%9D%B4%EA%B0%95%EC%9D%B8',
    'Card_number' : 20,
    'Like_Count': 0
}
db.player.insert_one(doc)

doc = {
    'image':'https://w.namu.la/s/031a840f9d26538a3791e3934e4b76e184e0a545f8e1f538d72171e43f923b96fa12046844c0cb0450ef0c521912203f33f00f215e1d6d5d4d176260e312a6675e1646b8e66d3247a5c2dccb2a64362fc6a9f8911c89389e5dec7e2d9ada48e450e79203284f9420555eab34bd3647b5',
    'Name' : '손흥민',
    'Position' : 'MF',
    'Team' : '토트넘 홋스퍼 FC',
    'Link' : 'https://namu.wiki/w/%EC%86%90%ED%9D%A5%EB%AF%BC',
    'Card_number' : 21,
    'Like_Count': 0
}
db.player.insert_one(doc)

doc = {
    'image':'https://w.namu.la/s/e395a9283bf9cfac714a6a120fcf330d10577b9ca4509e03b67ccda5268ffce3ded7a56755c572c66b1d87182dd666719226ae66816e499dfd60d971cc4bdfb057c4b9a3a74cf0bf645ff6fe7c34ea9e33d45baa3e3eb513df6e9483fba74fdb856acc19540dab51767d87557de892c9',
    'Name' : '황희찬',
    'Position' : 'MF',
    'Team' : '울버햄튼 원더러스 FC',
    'Link' : 'https://namu.wiki/w/%ED%99%A9%ED%9D%AC%EC%B0%AC',
    'Card_number' : 22,
    'Like_Count': 0
}
db.player.insert_one(doc)

doc = {
    'image':'https://w.namu.la/s/9127d41b8a984e61af0e367fe9b69e7eaeea12196adc33ad36831217e7b1c016d852b93e84a59443f1eed974ecb53b9ceccfe0a5555d4691ab6b99aa8d777068a5a564806b7f4bb9748ff3e13106fb0698855752133e265f9156b82b93270287bf11ba506b63b0a8f5f513d850df1997',
    'Name' : '나상호',
    'Position' : 'MF',
    'Team' : 'FC 서울',
    'Link' : 'https://namu.wiki/w/%EB%82%98%EC%83%81%ED%98%B8',
    'Card_number' : 23,
    'Like_Count': 0
}
db.player.insert_one(doc)

doc = {
    'image':'https://w.namu.la/s/462eeab76a725ac0b0e0715b4ef45e2b0a9c20389813c7475fc40986a45c505a1c8be1fbef5e18688e9811f12f6d7f68adcd04955159d8510db64241c754576d80506fe06cc8c320378ba1d09198ba720da0157251088ea599e0edecc11caa7292cbd9a315ae56e336b6b12daa11530a',
    'Name' : '송민규',
    'Position' : 'MF',
    'Team' : '전북 현대 모터스',
    'Link' : 'https://namu.wiki/w/%EC%86%A1%EB%AF%BC%EA%B7%9C',
    'Card_number' : 24,
    'Like_Count': 0
}
db.player.insert_one(doc)

doc = {
    'image':'https://w.namu.la/s/6e664cf5b478885264add876e10aa749f01740f02ece9c6efbd74ae3445da9f3a2acdeb1ee66f88ba1a9c72ae80d65f248779fef6758f78ed8b3085f04b2aa385e5ed254eee4b399de1a04555774be1718056cfec692ac2a669d77b2ab281998f0504ae85bd9e6ad877934883589e0d5',
    'Name' : '황의조',
    'Position' : 'FW',
    'Team' : '올림피아코스 FC',
    'Link' : 'https://namu.wiki/w/%ED%99%A9%EC%9D%98%EC%A1%B0',
    'Card_number' : 25,
    'Like_Count': 0
}
db.player.insert_one(doc)

doc = {
    'image':'https://w.namu.la/s/2c37cd36d423b4a6a972776816e532e65042e1094b85c8c1080daa02131b4f0297286d04b7fe8cfe5f03c629541bd42bf7b8c98216bd857d1beca1e75d26053983c4378b4edfdfc0f73d01dfd1a05b6ddccccb92a89510614bac7796c252fd275736de30b8ab03526e57fd63ac01fde1',
    'Name' : '조규성',
    'Position' : 'FW',
    'Team' : '전북 현대 모터스',
    'Link' : 'https://namu.wiki/w/%EC%A1%B0%EA%B7%9C%EC%84%B1',
    'Card_number' : 26,
    'Like_Count': 0
}
db.player.insert_one(doc)


