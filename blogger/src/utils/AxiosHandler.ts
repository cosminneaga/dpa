import Axios, { type AxiosInstance, type AxiosRequestConfig } from "axios";
import "vue3-toastify/dist/index.css";
import { toast } from "vue3-toastify";

export interface ApiInterface {
    get(path: string): Promise<ApiResponse> | undefined;
}

export interface ApiResponse {
    message: string;
    data: object;
    status: boolean;
}

/*
EXAMPLE USAGE
# plain
const result = await new this.Api(config: {}).get(`url`);
console.log("RESULT: ", result);

# body
const req = await new this.Api().post("/login", {
    email: this.email,
    password: this.password,
});
if (req) {
    execute code 
}

# params
const req = await new this.Api({
    params: {
        param: 'value'
    }
}).post("/login");
*/

export default class Api implements ApiInterface {
    client: AxiosInstance;
    cookie: any;

    constructor(config: AxiosRequestConfig = {}) {
        const service = Axios.create({
            baseURL: import.meta.env.VITE_BLOGGER_URL,
            headers: {
                "Content-Type": "application/json",
                "x-access-token": this.getCookie("X-Access-Token"),
            },
            timeout: 10 * 1000,
            ...config,
        });

        this.cookie = this.getCookie("X-Access-Token");
        this.client = service;
        this.client.interceptors.response.use(
            function (response: any) {
                if (response.data.status === 401) {
                    throw new Error("Not Authorized.");
                } else if (response.data.status === 404) {
                    throw new Error("Resource not found.");
                }
                return response;
            },
            function (error: any) {
                if (error.response) {
                    if (error.response.status === 404) {
                        throw new Error("Resource not found.");
                    } else if (error.response.status === 400) {
                        throw new Error(error.response.data.message.toString());
                    } else {
                        throw new Error("Something odd happend here!");
                    }
                }

                if (error.request) {
                    throw new Error(`${error.name}\n${error.code}\n${error.message}`);
                }
            }
        );
    }

    async get(url: string) {
        try {
            const req = await this.client.get(url);
            return req.data;
        } catch (e: any) {
            toast.error(e.message);
            return false;
        }
    }

    async post(url: string, body: object) {
        try {
            const req = await this.client.post(url, { ...body });
            return req.data;
            throw new Error("Hey Hoo");
        } catch (e: any) {
            toast.error(e.message);
            return false;
        }
    }

    async put(url: string, body: object) {
        try {
            const req = await this.client.put(url, { ...body });
            return req.data;
        } catch (e: any) {
            toast.error(e.message);
            return false;
        }
    }

    async delete(url: string) {
        try {
            const req = await this.client.delete(url);
            return req.data;
        } catch (e: any) {
            toast.error(e.message);
            return false;
        }
    }

    private getCookie(cookieName: string) {
        const cookie: any = {};
        document.cookie.split(";").forEach(function (el) {
            const [key, value] = el.split("=");
            cookie[key.trim()] = value;
        });
        return cookie[cookieName];
    }
}
