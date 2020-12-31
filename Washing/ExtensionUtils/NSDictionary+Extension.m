//
//  NSDictionary+Extension.m
//  Washing
//
//  Created by Quốc Tuyến on 12/2/20.
//  Copyright © 2020 QuocTuyen. All rights reserved.
//

#import "NSDictionary+Extension.h"

@implementation NSDictionary (Extension)

+ (NSDictionary *)dictionaryWithJsonifiedString:(NSString *)jsonified {
    NSAssert(jsonified && [jsonified isKindOfClass:[NSString class]], @"Invalid jsonified string!");
    NSData *data = [jsonified dataUsingEncoding:NSUTF8StringEncoding];
    return [NSJSONSerialization JSONObjectWithData:data
                                           options:kNilOptions
                                             error:nil];
}

@end
