import {BaseService} from "./BaseService";
import {PaginationModel, TypeElectionsNative} from "../types/TypeServices";

export class ElectionsNationalService extends BaseService<TypeElectionsNative> {
    public async getAllElectionsNative(pagination: PaginationModel): Promise<TypeElectionsNative[]> {
        return this.getAll("electionsnative", pagination);
    }
}