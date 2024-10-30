import {host} from '../config'


// type process_data
export default function StartReceiveData(){
  const startReceiveData = async ()=>{
    console.log('データ取得開始');
    const url = host + '/start_receiv'
    const response = await fetch(url)
  }
  return startReceiveData
}



  