import React from 'react';
import StartReceiveData from '../components/StartReceiveData';
import StopReceiveData from '../components/StopReceiveData';
import InsertData from '../components/InsertData';
import GetRightArm from '../components/GetDbData';
import StartCompare from '../components/StartCompare';
import StopCompare from '../components/StopCompare';


export default function PutDataButton(){
  const startReceiveData = StartReceiveData();
  const stopReceiveData = StopReceiveData();
  const insertDataTest = InsertData();
  const getRightArm = GetRightArm();
  const startCompare = StartCompare();
  const stopCompare = StopCompare();

  return (
    <>
      <div className="createDataButton">
          <button onClick= {startReceiveData}>データ採取開始</button>
        </div>
        <div className="stopDataButton">
          <button onClick={stopReceiveData}>データ採取終了</button>
      </div>
      <div className="insertDataTest">
          <button onClick={insertDataTest}>データ挿入テスト</button>
      </div>
      <hr></hr>
      <div className="readDataTest">
          <button onClick={getRightArm}>データ取得テスト</button>
      </div>
      <div className="compare">
          <button onClick={startCompare}>データ比較開始</button>
      </div>
      <div className="compare">
          <button onClick={stopCompare}>データ比較停止</button>
      </div>
    </>
  )

}