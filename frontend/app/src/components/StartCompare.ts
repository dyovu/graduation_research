import {host} from '../config'


// type process_data
export default function StartCompare(){
  const startCompare = async ()=>{
    console.log('データ取得開始');
    const url = host + '/start_compare'
    const response = await fetch(url)
  }
  return startCompare
}



  