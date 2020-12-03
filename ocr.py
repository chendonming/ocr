import base64
import requests


class BaiduOCR:
    def __init__(self, AK, SK, code_url, img_path):
        self.AK = AK
        self.SK = SK
        self.code_url = code_url
        self.img_path = img_path
        self.access_token = self.get_access_token()

    def get_access_token(self):
        token_host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={ak}&client_secret={sk}'.format(
            ak=self.AK, sk=self.SK)
        header = {'Content-Type': 'application/json; charset=UTF-8'}
        response = requests.post(url=token_host, headers=header)
        content = response.json()
        access_token = content.get("access_token")
        return access_token

    def getCode(self):
        header = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        def read_img():
            with open(self.img_path, "rb")as f:
                return base64.b64encode(f.read()).decode()

        image = read_img()
        response = requests.post(url=self.code_url, data={
                                 "image": image, "access_token": self.access_token}, headers=header)
        return response.json()


if __name__ == '__main__':
    AK = "o2dmI91tLrpKif98uIhzbVfU"  # 官网获取的AK
    SK = "t1z52AuDgqCZxB1Il6WaiyVbGr3kRGPT"  # 官网获取的SK
    code_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"  # 百度图片识别接口地址
    img_path = r""  # 识别图片的地址

    code_obj = BaiduOCR(AK=AK, SK=SK, code_url=code_url, img_path=img_path)
    res = code_obj.getCode()
    code = res.get("words_result")[0].get("words")
    print(res)
    print(code)
