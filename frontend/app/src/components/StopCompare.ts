import {host} from '../config'


// type process_data
export default function StopCompare(){
  const stopCompare = async ()=>{
    console.log('データ取得終了');
    const url = host + '/stop_compare'
    const response = await fetch(url)
    console.log(response.json());
  }
  return stopCompare
}



