//
//  NSArray+Extension.m
//  WSComponent
//
//  Created by Quốc Tuyến on 11/25/20.
//  Copyright © 2020 QuocTuyen. All rights reserved.
//

#import "NSArray+Extension.h"

@implementation NSArray (Extension)

- (void)each:(void (^)(id))block {
    [self enumerateObjectsUsingBlock:^(id obj, NSUInteger idx, BOOL *stop) {
        block(obj);
    }];
}

- (NSArray *)map:(id (^)(id obj))block {
    NSMutableArray *mutableArray = [NSMutableArray new];
    [self enumerateObjectsUsingBlock:^(id obj, NSUInteger idx, BOOL *stop) {
        id mappingObj = block(obj);
        if (!mappingObj) {
            return;
        }
        [mutableArray addObject:mappingObj];
    }];
    return [mutableArray copy];
}

- (NSArray *)flatMap:(id (^)(id obj))block {
    NSMutableArray *mutableArray = [NSMutableArray new];
    [self enumerateObjectsUsingBlock:^(id obj, NSUInteger idx, BOOL *stop) {
        id mappingObj = block(obj);
        if (mappingObj) {
            [mutableArray addObject:mappingObj];
        }
    }];
    return [mutableArray copy];
}

- (NSArray *)filter:(BOOL (^)(id obj))block {
    NSMutableArray *mutableArray = [NSMutableArray new];
    [self enumerateObjectsUsingBlock:^(id obj, NSUInteger idx, BOOL *stop) {
        if (block(obj) == YES) {
            [mutableArray addObject:obj];
        }
    }];
    return [mutableArray copy];
}

@end
