import {BaseService} from "./BaseService";
import {PaginationModel, TypeElectionsNational} from "../types/TypeServices";

export class ElectionsNationalService extends BaseService<TypeElectionsNational> {
    public async getAllElectionsNational(pagination: PaginationModel): Promise<TypeElectionsNational[]> {
        return this.getAll("electionsnational", pagination);
    }
}