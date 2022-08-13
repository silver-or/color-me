import { Article } from "@/modules/types";
import axios, { AxiosResponse } from "axios";
import {HOST_4000} from "@/components/common/Path"

const headers = {
    "Content-Type" : "application/json",
    Authorization: "JWT fefege...",
} 
export class ArticleController {
    

    async readBestColors ()  : Promise<any> {
        try{
            const response = await axios.get(`${HOST_4000}/best_colors`)
            return response.data
        } catch (err) {
            return(err)
        }
    }
    
    async readHairs ()  : Promise<any> {
        try{
            const response = await axios.get(`${HOST_4000}/hairs`)
            return response.data
        } catch (err) {
            return(err)
        }
    }

    async readLips ()  : Promise<any> {
        try{
            const response = await axios.get(`${HOST_4000}/lips`)
            return response.data
        } catch (err) {
            return(err)
        }
    }

    async readPersonalColors ()  : Promise<any> {
        try{
            const response = await axios.get(`${HOST_4000}/personal_colors`)
            return response.data
        } catch (err) {
            return(err)
        }
    }

    async readPosts ()  : Promise<any> {
        try{
            const response = await axios.get(`${HOST_4000}/posts`)
            return response.data
        } catch (err) {
            return(err)
        }
    }

    async readSkins ()  : Promise<any> {
        try{
            const response = await axios.get(`${HOST_4000}/skins`)
            return response.data
        } catch (err) {
            return(err)
        }
    }

    async readWorstColors ()  : Promise<any> {
        try{
            const response = await axios.get(`${HOST_4000}/worst_colors`)
            return response.data
        } catch (err) {
            return(err)
        }
    }

    async readYoutubers ()  : Promise<any> {
        try{
            const response = await axios.get(`${HOST_4000}/youtubers`)
            return response.data
        } catch (err) {
            return(err)
        }
    }

    /*
    async join(writeData: Article) : Promise<any>  {
        try {
            await axios.post(`${HOST_4000}/join`, writeData, {headers})            
        } catch (err) {
            return err;
        }
    }

    async login ()  : Promise<any> {
        try{
            const response = await axios.post(`${HOST_4000}/login`)
            return response.data
        } catch (err) {
            return(err)
        }
    }

    async logout ()  : Promise<any> {
        try{
            const response = await axios.post(`${HOST_4000}/logout`)
            return response.data
        } catch (err) {
            return(err)
        }
    }
    */
}

