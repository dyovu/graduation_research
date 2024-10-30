import {host} from '../config'


// type process_data
export default function InsertData(){
  const insertData = async ()=>{
    console.log('DBにデータ挿入中');
    const url = host + '/insert_data'
    const response = await fetch(url)
    console.log(response)
  }
  return insertData
}



