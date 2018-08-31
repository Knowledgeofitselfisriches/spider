# _*_ coding:utf-8 _*_

import requests
from bs4 import BeautifulSoup
import re


def wapper():
    url = 'https://www.pixiv.net/member_illust.php?id=4480830'
    headers = {
        "authority": "www.pixiv.net",
        "method": "GET",
        "path": "/member_illust.php?id=4480830",
        "scheme": "https",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "cookie": "p_ab_id=9; p_ab_id_2=3; _ga=GA1.2.1583587915.1524317009; PHPSESSID=1ef946c73a048f63843b9f40a34207ed; a_type=0; b_type=1; login_ever=yes; yuid=d5AHSEA46; __utmv=235335808.|2=login%20ever=yes=1^3=plan=normal=1^5=gender=male=1^6=user_id=13215431=1^9=p_ab_id=9=1^10=p_ab_id_2=3=1^11=lang=zh=1^20=webp_available=yes=1; __gads=ID=0fceb7d92c1161d1:T=1524464129:S=ALNI_MY3KyKm74q0skCFWgGwLAd4HD6LKA; privacy_policy_agreement=1; GMOSSP_USER=1UxrAJT99QnPCAH0; __utmc=235335808; OX_plg=pm; first_visit_datetime_pc=2018-05-29+01%3A53%3A29; __utmz=235335808.1527775140.47.7.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; c_type=24; module_orders_mypage=%5B%7B%22name%22%3A%22sketch_live%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22tag_follow%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22recommended_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22everyone_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22showcase%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22following_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22mypixiv_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22fanbox%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22featured_tags%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22contests%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22user_events%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22sensei_courses%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22spotlight%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22booth_follow_items%22%2C%22visible%22%3Atrue%7D%5D; ki_r=; ki_u=b8baefbf-97ce-7bed-90bc-2c76; ki_s=189784%3A1.0.0.0.1; _td=132514fe-2942-4c71-a6f7-f0040d4eae64; ki_t=1533485850491%3B1534955994295%3B1534955994295%3B11%3B16; limited_ads=%7B%22header%22%3A%22%22%2C%22responsive%22%3A%22%22%7D; is_sensei_service_user=1; __utma=235335808.1583587915.1524317009.1535649014.1535696304.127; tag_view_ranking=RTJMXD26Ak~Lt-oEicbBr~bXMh6mBhl8~rqnJSF7cpq~tgP8r-gOe_~K8esoIs2eW~BU9SQkS-zU~G_f4j5NH8i~VAB5BXKOPk~vOJFVciNcS~65aiw_5Y72~zyKU3Q5L4C~0Sds1vVNKR~XtvEexnwlO~Ie2c51_4Sp~KN7uxuR89w~y8GNntYHsi~THI8rtfzKo~q303ip6Ui5~J4vCOcB09W~nQRrj5c6w_~qtVr8SCFs5~YRDwjaiLZn~HZrKakXeye~fg8EOt4owo~azESOjmQSV~osjGBvsNDJ~LJo91uBPz4~Is0SiXyaWb~SucrrDZWra~2_IEt5mZob~4YKZYZCm1J~MhuNMsFpmN~sLQ8trav9X~kHJk-sR8-P~RcahSSzeRf~Ac_mADAVwx~eAor-vtHcM~jH0uD88V6F~PiMMyAmaD5~QKSUyLo4US~CrFcrMFJzz~ay54Q_G6oX~mzJgaDwBF5~BtXd1-LPRH~0O4JAvysMP~TCnz1buGzH~5trkxLyw0G~0YMUbkKItS~TUVB-oxjcR~qiO14cZMBI~w8ffkPoJ_S~ETjPkL0e6r~mf6rICH32i~E8plmQ7kUK~yzHYrrR9mN~RokSaRBUGr~UOfaO1Dqq-~_pwIgrV8TB~gooMLQqB9a~fbUyQrXMR3~sylWziJEvL~gpglyfLkWs~HY55MqmzzQ~xZ6jtQjaj9~NpsIVvS-GF~Y58bK2ZcH-~j3leh4reoN~0D4os7LO_T~AjBDLpRc95~spPqEvHEF2~ePN3h1AXKX~5MpL7lq7f6~mqN8uI2sx3~Df5EnHThdj~lkMC6APm-e~5oPIfUbtd6~f4V1aCLsyM~JXmGXDx4tL~cbmDKjZf9z~-sp-9oh8uv~WMZHvzbG1g~Jg_BKFcFMF~LHOQaWyQpt~aKhT3n4RHZ~Nx1CukYg8-~28gdfFXlY7~f-c_0dUV8c~CiSfl_AE0h~zyGISprTEN~f-Ku-oELiH~37s8SdOvcg~faHcYIP1U0~GUjcjgECvl~GYJKiJr9G2~_iaP-J1xu4~W5CXrSPrfn~aUKGRzPd6e~Kw3rxm81BS~hsH6XiBGKl; __utmb=235335808.3.9.1535696338057",
        "pragma": "no-cache",
        "referer": "https://www.pixiv.net/member_illust.php?mode=medium&illust_id=67628900",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    }
    response = requests.get(url, headers=headers)
    print(response.status_code)
    content = response.text
    print(content)

if __name__ == '__main__':
    wapper()