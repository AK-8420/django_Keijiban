document.addEventListener('DOMContentLoaded', function () {
    // 各所にイベントリスナーを設置する．これは，HTML読み込み完了時に動作する．

    class webConnector extends XMLHttpRequest {
        constructor() {
            super();
            this.addEventListener('load', function () {
                let data = this.response;
                show(data, id);
            }, false); //通信成功時処理
            this.addEventListener('error', function () {
                window.alert(this.url + "との通信に失敗しました");
            }, false); //通信失敗時処理
        }
    }
    let xhr = new webConnector();
    let id = { past:0 }; // どこのIDまで表示したか
    let board = document.getElementById('board');
    let se_update = new Audio("SE/消失・ぱちんっ.mp3");
    let se_send = new Audio("SE/消失・しゅぽん.mp3");
    se_update.volume = 0.5;
    se_send.volume = 0.5;

    // 最初に掲示板に書き込みがあるかチェック
    let url = "./cgi-bin/Board.py?" + "flag=" + 0 + "&id_past=" + id.past;
    xhr.open("GET", url);
    xhr.responseType = 'json';
    xhr.url = url;
    xhr.send(null);

    document.getElementById('update').addEventListener('click', function () {
        // 更新ボタンが押されたときに発火するイベントリスナー
        se_update.play();
        let url = "./cgi-bin/Board.py?" + "flag=" + 0 + "&id_past=" + id.past;
        xhr.open("GET", url);
        xhr.responseType = 'json';
        xhr.url = url;
        xhr.send(null);
    }, false);
    document.getElementById('send').addEventListener('click', function () {
        // 投稿ボタンが押されたときに発火するイベントリスナー
        let namae = document.getElementById('namae').value;
        let message = document.getElementById('message').value;
        let error = document.getElementById('error');

        if(message.length == 0){
            error.textContent = "何かメッセージを入力してください";
        }
        else{
            se_send.play();
            error.textContent = null;
            if(namae.length == 0) namae = '名無しさん';

            //改行を改行タグに置き換える
            message = message.split("\n").join("<br>");
            //オプションの反映
            let options = document.getElementsByName('option');
            let temp = "";
            for(o of options){
                if(o.checked){
                    switch(o.value){
                        case "big":
                            temp += "op_big "
                            break;
                        case "bold":
                            temp += "op_bold "
                            break;
                        case "ita":
                            temp += "op_ita "
                            break;
                    }
                }
            }
            if(temp.length != 0){
                temp = temp.slice(0,-1); //末尾の余計な空白を消す
                message = "<span class='" + temp + "'>" + message + "</span>";
            }

            //送信
            let url = "./cgi-bin/Board.py?" + "flag=" + 1 + "&name=" + namae + "&mes=" + message + "&id_past=" + id.past;
            xhr.open("GET", url);
            xhr.responseType = 'json';
            xhr.url = url;
            xhr.send(null);
        }
    }, false);
}, false);

function show(data, id) {
    if (data.length != 0) {
        console.log(data);
        let def = document.getElementById('default');
        if(def != null){
            //「まだ書き込みがありません」という文を削除
            board.removeChild(def);
        }

        for (let d of data){
            let p = document.createElement('p');
            let h = document.createElement('span');
            h.className = "h";

            let D = new Date(d['time'] * 1000);
            let date = D.getFullYear() + '年' + (D.getMonth()+1) + "月" + D.getDate() + '日 ';
            date += ('00'+ D.getHours()).slice(-2)+':'+('00'+ D.getMinutes()).slice(-2)+':'+('00'+ D.getSeconds()).slice(-2);

            //名前と日付（色付き）
            h.appendChild(document.createTextNode(d['id'] + '．' + d['name'] + '：' + date));
            p.appendChild(h);
            board.appendChild(p);

            //メッセージ
            p = document.createElement('p');
            p.innerHTML = d['message'];
            board.appendChild(p);
        }
        id.past += data.length;
        console.log("id.past = " + id.past);
    }
}
