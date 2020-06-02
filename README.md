# Flask-Web-API

## Environment

- windows 8
- python 3.6
- Visual Studio Code
- Libray 請參考 requirements.txt

## Summary

透過 Flask 快速搭建一個簡單的 web api

利用 FinMind 所提供的股價資料庫來建立 api，避免使用者直接對 DB 撈資料

讓 user 只要輸入資料名稱、股價代碼、時間即可獲取該資料

最後再透過 test.py 來測試 api 是否符合需求

## RESTful API

HTTP 協定中，定義了多種不同的 method 做為服務的請求方法，常見如下五種:

    GET: 取得服務的資料或是狀態。（safe & idempotent）
    POST: 將原先沒有的資料去做一筆新增的動作
    PUT: 利用更新的方式於"指定位置"新增一項資料，像是複製檔案貼上。 （idempotent）
    PATCH: 在現有的資料欄位中，增加或部分更新一筆新的資料，就是一般常見的修改。
    DELETE: 指定資料刪除。 （idempotent）

- safe: 該操作不會改變原本的資源狀態，並且同樣的結果是可以被快取（Cache）的，EX: 訂單查詢
- idempotent: 該操作不管做1遍、2遍或多遍，都會得到同樣的資源狀態結果
- POST/PUT 都可以用來新增
- PATCH/PUT 都可以用來修改

在 Http 的協定下，每一種呼叫方式都會有一種他專屬的特殊定義，也就是說不同的方法就是對同一件事情做不同的操作。

像是在開發 API 時，會透過一個 url 來進行讀取資料或上傳資料，而可以理解成每一個 url 是一個專屬服務的窗口

**在開發 API 時沒有一定要照著上面的定義敘述建立，但如果你符合的話，你可以將它稱作 Restful API**

REST 全名 Resource Representational State Transfer ，可譯為具象狀態傳輸，若是把各個單字拆開來解釋的話即如下：

- Resource：資源
- Representational：表現形式，如 JSON，XML ...
- State Transfer：狀態變化。即上述講到的可利用 HTTP 動詞們來做呼叫

REST 指的是網路中 Client 端和 Server 端的一種呼叫服務形式，透過既定的規則，滿足約束條件和原則的應用程式設計，對資源的操作包括獲取、創建、修改和刪除資源，這些操作就是依照我們前面所提到的 HTTP Method: GET、POST、PUT、PATCH和DELETE。這正好會對應到資料庫基本操作 CRUD。

CRUD 為 Create(新增)、Read(讀取)、Update(更新)與Delete(刪除)的縮寫。

## Reference

- [輕鬆學習 Python：使用 Flask 創建 Web API](https://medium.com/datainpoint/flask-web-api-quickstart-3b13d96cccc2)

- [REST APIs with Flask 系列教學文 [1]](https://medium.com/@twilightlau94/rest-apis-with-flask-%E7%B3%BB%E5%88%97%E6%95%99%E5%AD%B8%E6%96%87-1-5405216d3166)

- [寫给新手看的 Flask+uwsgi+Nginx+Ubuntu 部署教程](https://knarfeh.com/2016/06/11/%E5%86%99%E7%BB%99%E6%96%B0%E6%89%8B%E7%9C%8B%E7%9A%84Flask+uwsgi+Nginx+Ubuntu%E9%83%A8%E7%BD%B2%E6%95%99%E7%A8%8B/?fbclid=IwAR0jsMX4qDhMBpyj3H84Xfc6tIJre12179Kgc1EFlfzcnpAL2zeo7GunK_c)

- [[不是工程師] 休息(REST)式架構? 寧靜式(RESTful)的Web API是現在的潮流？](https://progressbar.tw/posts/53)