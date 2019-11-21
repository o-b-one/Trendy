import { ModelName, MongoModel } from '@sugoi/mongodb';

@ModelName("data")
export class DataModel extends MongoModel {
    public get id() {
            return this._id.toString();
    }

    constructor() {
        super();
    }

}