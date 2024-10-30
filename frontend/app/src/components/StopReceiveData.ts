import {host} from '../config'


// type process_data
export default function StopReceiveData(){
  const stopReceiveData = async ()=>{
    console.log('データ取得終了');
    const url = host + '/stop_receiv'
    const response = await fetch(url)
    console.log(response.json());
  }
  return stopReceiveData
}



