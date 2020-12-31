//
//  WSMacros.h
//  Washing
//
//  Created by Quốc Tuyến on 11/23/20.
//  Copyright © 2020 QuocTuyen. All rights reserved.
//

#ifndef WSMacros_h
#define WSMacros_h

#define WEAKSELF    __weak __typeof(self) weakSelf = self;
#define STRONGSELF  __strong __typeof(weakSelf) strongSelf = weakSelf;

#define isValidClass(_obj, _className)      (_obj != nil && [_obj isKindOfClass:[_className class]])
#define isNotValidClass(_obj, _className)   !isValidClass(_obj, _className)

#define isNotEmptyStr(str)      (str && [str isKindOfClass:[NSString class]] && ((NSString*)str).length>0)
#define isNotEmptyArr(arr)      (arr && [arr isKindOfClass:[NSArray class]] && ((NSArray*)arr).count>0)
#define isNotEmptyDict(dict)    (dict && [dict isKindOfClass:[NSDictionary class]] && ((NSDictionary*)dict).count>0)

#define isEmptyString(src)      !isNotEmptyStr(src)
#define isEmptyArray(arr)       !isNotEmptyArr(arr)
#define isEmptyDict(dict)       !isNotEmptyDict(dict)

#define safeExec(block, ...) block ? block(__VA_ARGS__) : nil
#define sharedInstance(className, instanceName) @property(class, nonatomic, strong, readonly) className *instanceName;

#endif /* WSMacros_h */
