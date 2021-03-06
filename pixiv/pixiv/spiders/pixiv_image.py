# -*- coding: utf-8 -*-
import scrapy


class PixivImageSpider(scrapy.Spider):
    name = 'pixiv_image'
    allowed_domains = ['www.pixiv.net']
    id = 6723391
    page = 1
    url = 'https://www.pixiv.net/member.php?id={}'
    cookies = {
        "p_ab_id": "9",
        "p_ab_id_2": "3",
        "_ga": "GA1.2.1583587915.1524317009",
        "PHPSESSID": "1ef946c73a048f63843b9f40a34207ed",
        "a_type": "0",
        "b_type": "1",
        "login_ever": "yes",
        "yuid": "d5AHSEA46",
        "__utmv=235335808.|2=login%20ever=yes=1^3=plan=normal=1^5=gender=male=1^6=user_id=13215431=1^9=p_ab_id=9=1^10=p_ab_id_2=3=1^11=lang=zh=1^20=webp_available=yes": "1",
        "__gads=ID=0fceb7d92c1161d1:T=1524464129:S": "ALNI_MY3KyKm74q0skCFWgGwLAd4HD6LKA",
        "privacy_policy_agreement": "1",
        "GMOSSP_USER": "1UxrAJT99QnPCAH0",
        "__utmc": "235335808",
        "OX_plg": "pm",
        "first_visit_datetime_pc": "2018-05-29+01%3A53%3A29",
        "__utmz=235335808.1527775140.47.7.utmcsr=baidu|utmccn=(organic)|utmcmd": "organic",
        "c_type": "24",
        "module_orders_mypage": "%5B%7B%22name%22%3A%22sketch_live%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22tag_follow%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22recommended_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22everyone_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22showcase%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22following_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22mypixiv_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22fanbox%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22featured_tags%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22contests%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22user_events%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22sensei_courses%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22spotlight%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22booth_follow_items%22%2C%22visible%22%3Atrue%7D%5D",
        "ki_r": '',
        "ki_u": "b8baefbf-97ce-7bed-90bc-2c76",
        "_td": "132514fe-2942-4c71-a6f7-f0040d4eae64",
        "ki_s": "189784%3A1.0.0.0.1%3B190555%3A1.0.0.0.1",
        "is_sensei_service_user": "1",
        "__utma": "235335808.1583587915.1524317009.1536244784.1536312745.137",
        "ki_t": "1533485850491%3B1536312783769%3B1536312783769%3B15%3B20",
        "limited_ads": "%7B%22header%22%3A%22%22%2C%22responsive%22%3A%226832~6831~6829%22%2C%22illust_responsive%22%3A%22%22%7D",
        "tag_view_ranking": "RTJMXD26Ak~tgP8r-gOe_~Lt-oEicbBr~zyKU3Q5L4C~BU9SQkS-zU~K8esoIs2eW~VAB5BXKOPk~bXMh6mBhl8~KN7uxuR89w~vOJFVciNcS~azESOjmQSV~jH0uD88V6F~RcahSSzeRf~Ie2c51_4Sp~XtvEexnwlO~LJo91uBPz4~Bd2L9ZBE8q~faHcYIP1U0~nQRrj5c6w_~BaQprNPH_K~Z4hQZu-rU-~CrFcrMFJzz~y8GNntYHsi~65aiw_5Y72~NpsIVvS-GF~qtVr8SCFs5~x_jB0UM4fe~0Sds1vVNKR~AjBDLpRc95~mzJgaDwBF5~G_f4j5NH8i~SucrrDZWra~yVQkQ91Qkw~HY55MqmzzQ~9V46Zz_N_N~-sp-9oh8uv~spPqEvHEF2~cbmDKjZf9z~5trkxLyw0G~sylWziJEvL~OT4SuGenFI~gpglyfLkWs~YRDwjaiLZn~w8ffkPoJ_S~kHJk-sR8-P~Y5Tw-5iHPe~gooMLQqB9a~eAor-vtHcM~mPFmmA9wY_~rELYgW0qN3~ay54Q_G6oX~4YKZYZCm1J~pzzjRSV6ZO~fbUyQrXMR3~-StjcwdYwv~YX3tU8uRAA~MhuNMsFpmN~ZTBAtZUDtQ~5RvyKm3yea~kP7msdIeEU~zIv0cf5VVk~j3leh4reoN~MhieHQxNXo~TUVB-oxjcR~Is0SiXyaWb~q303ip6Ui5~5oPIfUbtd6~_pwIgrV8TB~Hry6GxyqEm~XDEWeW9f9i~EUwzYuPRbU~BtXd1-LPRH~qiO14cZMBI~ZXRBqRlFWu~0YMUbkKItS~TCnz1buGzH~aNqTPYQ7NR~bSSkEPgu92~orHGhUVIu0~fAH-uXqd9x~f4V1aCLsyM~nRp2ZLPLbj~3mLXnunyNA~JtHr1OyMVc~ixJ21_XZkb~InBpdMUtQZ~ICsokp9RfZ~ePN3h1AXKX~92z8RZmGQ6~FqVQndhufZ~C9_ZtBtMWU~ZSc1yK2SWA~xVHdz2j0kF~I3HFXzGTQb~S4kJj1kz1Z~GmCzj7c06U~p7TjX6YIQJ~3K-NVQVfzS~PiMMyAmaD5~0D4os7LO_T",
        "__utmb": "235335808.43.9.1536316468995"

    }

    # start_urls = [url.format(id)]
    def start_requests(self):
        yield scrapy.Request(self.url.format(id), cookies=self.cookies, callback=self.parse)

    def parse(self, response):
        print(response.url)
