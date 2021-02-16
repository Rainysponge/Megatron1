// 疑问词
有哪些 :- S\(S/NP)\N : (lambda $0:<e,t> (lambda $1:<e,t> (lambda $2:e (and:<t*,t> ($0 $2) ($1 $2)))))
有哪些 :- S/(S/NP)/N : (lambda $0:<e,t> (lambda $1:<e,t> (lambda $2:e (and:<t*,t> ($0 $2) ($1 $2)))))
哪些 :- S/(S/NP)/N : (lambda $0:<e,t> (lambda $1:<e,t> (lambda $2:e (and:<t*,t> ($0 $2) ($1 $2)))))
哪个 :- S/(S/NP)/N : (lambda $0:<e,t> (lambda $1:<e,t> (lambda $2:e (and:<t*,t> ($0 $2) ($1 $2)))))


// 动词
得 :- (S/NP)/NP : (lambda $0:e (lambda $1:e (illness:<ill,<pat,t>> $0 $1)))
就诊 :- (S/NP)\NP : (lambda $0:e (lambda $1:e (visit:<dp,<pat,t>> $0 $1)))
做 :- (S/NP)/NP : (lambda $0:e (lambda $1:e (treatment:<treat,<pat,t>> $0 $1)))
诊断 :- (S/NP)/NP : (lambda $0:e (lambda $1:e (illness:<ill,<pat,t>> $0 $1)))
结果 :- (S/NP)/NP : (lambda $0:e (lambda $1:e (result:<res,<pat,t>> $0 $1)))
检查 :- (S/NP)/NP : (lambda $0:e (lambda $1:e (treatment:<treat,<pat,t>> $0 $1)))
年龄 :- (S/NP)/NP : (lambda $0:e (lambda $1:e (age:<age,<pat,t>> $0 $1)))

手术 :- (S/NP)/NP : (lambda $0:e (lambda $1:e (result:<res,<pat,t>> $0 $1)))



// 形容词
女 :- N/N : (lambda $0:<e,t> (lambda $1:e (and:<t*,t> ($0 $1) (gender:<gen,<pat,t>> 女:gen $1))))
女性 :- N/N : (lambda $0:<e,t> (lambda $1:e (and:<t*,t> ($0 $1) (gender:<gen,<pat,t>> 女:gen $1))))
男 :- N/N : (lambda $0:<e,t> (lambda $1:e (and:<t*,t> ($0 $1) (gender:<gen,<pat,t>> 男:gen $1))))
男性 :- N/N : (lambda $0:<e,t> (lambda $1:e (and:<t*,t> ($0 $1) (gender:<gen,<pat,t>> 男:gen $1))))
新型冠状肺炎 :- N/N : (lambda $0:<e,t> (lambda $1:e (and:<t*,t> ($0 $1) (illness:<ill,<pat,t>> 新型冠状肺炎:ill $1))))


// 名词
患者 :- N : patient:<pat,t>
人 :- N : patient:<pat,t>
病人 :- N : patient:<pat,t>
