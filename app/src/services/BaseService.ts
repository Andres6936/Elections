import {PaginationModel} from "../types/TypeServices";

export class BaseService<T> {
    protected readonly BASE_URL: string = "http://127.0.0.1:8000";

    public async getAll(endpoint: string, pagination: PaginationModel): Promise<T[]> {
        const stream = await fetch(`${this.BASE_URL}/${endpoint}?skip=${pagination.skip}&limit=${pagination.limit}`, {
            method: "GET",
        })
        return stream.json()
    }
}