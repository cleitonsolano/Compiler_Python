
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftEPARENDPARENleftEOUleftMAIORMENORMAIORIGUALMENORIGUALIGUALDIFERENTEleftMAISMENOSleftMULTIPLICACAODIVIDErightEXCLAMACAOINTERROGACAOASPASD ATRIBUICAO CAR DCHAVES DCOCHETE DIFERENTE DIVIDE DOISP DPAREN E ECHAVES ECOCHETE ENQUANTO ENTAO EPAREN ESCREVA EXCLAMACAO EXECUTE IGUAL INT INTERROGACAO LEIA MAIOR MAIORIGUAL MAIS MENOR MENORIGUAL MENOS MOD MULTIPLICACAO NOME NORMALSTRING NOVALINHA NUMERO OU PROGRAMA PVIRGULA RETORNE SE SENAO VIRGULAPrograma : DeclFuncVar DeclProg DeclFuncVar : Tipo NOME DeclVar PVIRGULA DeclFuncVar\n\t\t\t\t\t| Tipo NOME ECOCHETE INT DCOCHETE DeclVar PVIRGULA DeclFuncVar\n\t\t\t\t\t| Tipo NOME DeclFunc DeclFuncVar\n\t\t\t\t\t|  DeclProg : PROGRAMA Bloco DeclVar : VIRGULA NOME DeclVar \n\t\t\t\t| VIRGULA NOME ECOCHETE INT DCOCHETE DeclVar\n\t\t\t\t|  DeclFunc : EPAREN ListaParametros DPAREN Bloco ListaParametros : \n\t\t\t\t\t\t| ListaParametrosCont  ListaParametrosCont : Tipo NOME\n\t\t\t\t\t\t\t| Tipo NOME ECOCHETE DCOCHETE\n\t\t\t\t\t\t\t| Tipo NOME VIRGULA ListaParametrosCont\n\t\t\t\t\t\t\t| Tipo NOME ECOCHETE DCOCHETE VIRGULA ListaParametrosCont  Bloco : ECHAVES ListaDeclVar ListaComando DCHAVES\n\t\t\t| ECHAVES ListaDeclVar DCHAVES  ListaDeclVar : \n\t\t\t\t\t| Tipo NOME DeclVar PVIRGULA ListaDeclVar \n\t\t\t\t\t| Tipo NOME ECOCHETE INT DCOCHETE DeclVar PVIRGULA ListaDeclVar  Tipo : INT\n\t\t\t | CAR  ListaComando : Comando\n\t\t\t\t\t| Comando ListaComando  Comando : PVIRGULA\n\t\t\t\t| RETORNE Expr PVIRGULA\n\t\t\t\t| LEIA LValueExpr PVIRGULA\n\t\t\t\t| ESCREVA Expr PVIRGULA\n\t\t\t\t| ESCREVA ASPASD NORMALSTRING ASPASD PVIRGULA\n\t\t\t\t| NOVALINHA PVIRGULA\n\t\t\t\t| SE EPAREN Expr DPAREN ENTAO Comando\n\t\t\t\t| SE EPAREN Expr DPAREN ENTAO Comando SENAO Comando\n\t\t\t\t| ENQUANTO EPAREN Expr DPAREN EXECUTE Comando\n\t\t\t\t| Bloco Expr : AssignExpr AssignExpr : CondExpr\n\t\t\t\t| LValueExpr IGUAL AssignExpr  CondExpr : OrExpr\n\t\t\t\t| OrExpr INTERROGACAO Expr DOISP CondExpr  OrExpr : OrExpr OU AndExpr\n\t\t\t| AndExpr  AndExpr : AndExpr E EqExpr\n\t\t\t\t| EqExpr  EqExpr : EqExpr ATRIBUICAO DesigExpr\n\t\t\t   | EqExpr DIFERENTE DesigExpr\n\t\t\t   | DesigExpr  DesigExpr : DesigExpr MENOR AddExpr\n\t\t\t\t  | DesigExpr MAIOR AddExpr\n\t\t\t\t  | DesigExpr MAIORIGUAL AddExpr\n\t\t\t\t  | DesigExpr MENORIGUAL AddExpr\n\t\t\t\t  | AddExpr  AddExpr : AddExpr MAIS MulExpr\n                | AddExpr MENOS MulExpr\n                | MulExpr  MulExpr : MulExpr MULTIPLICACAO UnExpr\n\t\t\t\t| MulExpr DIVIDE UnExpr\n\t\t\t\t| MulExpr MOD UnExpr\n\t\t\t\t| UnExpr  UnExpr : MENOS PrimExpr\n\t\t\t   | EXCLAMACAO PrimExpr\n\t\t\t   | PrimExpr  LValueExpr : NOME ECOCHETE Expr DCOCHETE\n\t\t\t\t   | NOME  PrimExpr : NOME EPAREN ListExpr DPAREN\n\t\t\t\t| NOME EPAREN DPAREN\n\t\t\t\t| NOME ECOCHETE Expr DCOCHETE\n\t\t\t\t| NOME\n\t\t\t\t| NUMERO\n\t\t\t\t| CAR\n\t\t\t\t| INT\n\t\t\t\t| EPAREN Expr DPAREN  ListExpr : AssignExpr\n\t\t\t\t| ListExpr VIRGULA AssignExpr '
    
_lr_action_items = {'PROGRAMA':([0,2,13,18,20,26,37,43,75,108,139,],[-5,7,-5,-5,-4,-18,-2,-17,-10,-5,-3,]),'INT':([0,10,12,13,15,18,26,29,31,40,43,56,59,60,69,70,72,75,77,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,101,106,108,131,141,142,145,158,],[4,4,19,4,4,4,-18,63,63,74,-17,63,63,63,63,63,107,-10,4,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,4,4,63,4,63,63,4,]),'CAR':([0,10,13,15,18,26,29,31,43,56,59,60,69,70,75,77,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,101,106,108,131,141,142,145,158,],[5,5,5,5,5,-18,62,62,-17,62,62,62,62,62,-10,5,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,5,5,62,5,62,62,5,]),'$end':([1,6,9,26,43,],[0,-1,-6,-18,-17,]),'NOME':([3,4,5,14,17,24,29,30,31,56,59,60,69,70,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,101,131,142,145,],[8,-22,-23,21,36,42,50,65,50,97,97,50,50,50,50,50,97,50,50,97,97,97,97,97,97,97,97,97,97,97,97,50,50,97,50,]),'ECHAVES':([7,10,16,26,27,28,35,41,43,68,78,100,102,106,137,148,149,150,156,157,158,159,160,161,],[10,-19,10,-18,10,-26,-35,10,-17,-31,-27,-28,-29,-19,-20,-30,10,10,-32,-34,-19,10,-21,-33,]),'ECOCHETE':([8,21,36,42,50,65,97,],[12,40,72,76,82,101,131,]),'VIRGULA':([8,21,36,38,42,47,49,50,51,52,53,54,55,57,58,61,62,63,96,97,98,109,110,112,114,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,132,138,143,144,153,154,155,],[14,14,14,14,77,-37,-39,-68,-42,-44,-47,-52,-55,-59,-62,-69,-70,-71,-60,-68,-61,14,141,-38,-41,145,-66,-73,-43,-45,-46,-48,-49,-50,-51,-53,-54,-56,-57,-58,-72,14,-67,-65,-40,-74,-67,]),'PVIRGULA':([8,10,11,16,21,26,27,28,32,35,36,38,39,43,45,46,47,49,50,51,52,53,54,55,57,58,61,62,63,64,65,66,68,71,73,78,96,97,98,100,102,106,109,112,114,117,119,120,121,122,123,124,125,126,127,128,129,130,132,134,137,138,140,143,144,147,148,149,150,151,153,155,156,157,158,159,160,161,],[-9,-19,18,28,-9,-18,28,-26,68,-35,-9,-9,-7,-17,78,-36,-37,-39,-68,-42,-44,-47,-52,-55,-59,-62,-69,-70,-71,100,-64,102,-31,106,108,-27,-60,-68,-61,-28,-29,-19,-9,-38,-41,-66,-43,-45,-46,-48,-49,-50,-51,-53,-54,-56,-57,-58,-72,148,-20,-9,-8,-67,-65,-63,-30,28,28,158,-40,-67,-32,-34,-19,28,-21,-33,]),'EPAREN':([8,29,31,33,34,50,56,59,60,69,70,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,97,101,131,142,145,],[15,60,60,69,70,83,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,83,60,60,60,60,]),'DCHAVES':([10,16,25,26,27,28,35,43,44,68,78,100,102,106,137,148,156,157,158,160,161,],[-19,26,43,-18,-24,-26,-35,-17,-25,-31,-27,-28,-29,-19,-20,-30,-32,-34,-19,-21,-33,]),'RETORNE':([10,16,26,27,28,35,43,68,78,100,102,106,137,148,149,150,156,157,158,159,160,161,],[-19,29,-18,29,-26,-35,-17,-31,-27,-28,-29,-19,-20,-30,29,29,-32,-34,-19,29,-21,-33,]),'LEIA':([10,16,26,27,28,35,43,68,78,100,102,106,137,148,149,150,156,157,158,159,160,161,],[-19,30,-18,30,-26,-35,-17,-31,-27,-28,-29,-19,-20,-30,30,30,-32,-34,-19,30,-21,-33,]),'ESCREVA':([10,16,26,27,28,35,43,68,78,100,102,106,137,148,149,150,156,157,158,159,160,161,],[-19,31,-18,31,-26,-35,-17,-31,-27,-28,-29,-19,-20,-30,31,31,-32,-34,-19,31,-21,-33,]),'NOVALINHA':([10,16,26,27,28,35,43,68,78,100,102,106,137,148,149,150,156,157,158,159,160,161,],[-19,32,-18,32,-26,-35,-17,-31,-27,-28,-29,-19,-20,-30,32,32,-32,-34,-19,32,-21,-33,]),'SE':([10,16,26,27,28,35,43,68,78,100,102,106,137,148,149,150,156,157,158,159,160,161,],[-19,33,-18,33,-26,-35,-17,-31,-27,-28,-29,-19,-20,-30,33,33,-32,-34,-19,33,-21,-33,]),'ENQUANTO':([10,16,26,27,28,35,43,68,78,100,102,106,137,148,149,150,156,157,158,159,160,161,],[-19,34,-18,34,-26,-35,-17,-31,-27,-28,-29,-19,-20,-30,34,34,-32,-34,-19,34,-21,-33,]),'DPAREN':([15,22,23,42,46,47,49,50,51,52,53,54,55,57,58,61,62,63,83,96,97,98,99,104,105,110,111,112,114,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,132,143,144,152,153,154,155,],[-11,41,-12,-13,-36,-37,-39,-68,-42,-44,-47,-52,-55,-59,-62,-69,-70,-71,117,-60,-68,-61,132,135,136,-14,-15,-38,-41,144,-66,-73,-43,-45,-46,-48,-49,-50,-51,-53,-54,-56,-57,-58,-72,-67,-65,-16,-40,-74,-67,]),'DCOCHETE':([19,46,47,49,50,51,52,53,54,55,57,58,61,62,63,74,76,96,97,98,107,112,114,115,117,119,120,121,122,123,124,125,126,127,128,129,130,132,133,143,144,146,153,155,],[38,-36,-37,-39,-68,-42,-44,-47,-52,-55,-59,-62,-69,-70,-71,109,110,-60,-68,-61,138,-38,-41,143,-66,-43,-45,-46,-48,-49,-50,-51,-53,-54,-56,-57,-58,-72,147,-67,-65,155,-40,-67,]),'SENAO':([26,28,35,43,68,78,100,102,148,156,157,161,],[-18,-26,-35,-17,-31,-27,-28,-29,-30,159,-34,-33,]),'MENOS':([29,31,50,54,55,57,58,60,61,62,63,69,70,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,101,117,122,123,124,125,126,127,128,129,130,131,132,142,143,144,145,155,],[56,56,-68,92,-55,-59,-62,56,-69,-70,-71,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,-60,-68,-61,56,-66,92,92,92,92,-53,-54,-56,-57,-58,56,-72,56,-67,-65,56,-67,]),'EXCLAMACAO':([29,31,60,69,70,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,101,131,142,145,],[59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,]),'NUMERO':([29,31,56,59,60,69,70,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,101,131,142,145,],[61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,]),'ASPASD':([31,103,],[67,134,]),'DOISP':([46,47,49,50,51,52,53,54,55,57,58,61,62,63,96,97,98,112,113,114,117,119,120,121,122,123,124,125,126,127,128,129,130,132,143,144,153,155,],[-36,-37,-39,-68,-42,-44,-47,-52,-55,-59,-62,-69,-70,-71,-60,-68,-61,-38,142,-41,-66,-43,-45,-46,-48,-49,-50,-51,-53,-54,-56,-57,-58,-72,-67,-65,-40,-67,]),'IGUAL':([48,50,143,],[79,-64,-63,]),'INTERROGACAO':([49,50,51,52,53,54,55,57,58,61,62,63,96,97,98,114,117,119,120,121,122,123,124,125,126,127,128,129,130,132,143,144,155,],[80,-68,-42,-44,-47,-52,-55,-59,-62,-69,-70,-71,-60,-68,-61,-41,-66,-43,-45,-46,-48,-49,-50,-51,-53,-54,-56,-57,-58,-72,-67,-65,-67,]),'OU':([49,50,51,52,53,54,55,57,58,61,62,63,96,97,98,114,117,119,120,121,122,123,124,125,126,127,128,129,130,132,143,144,155,],[81,-68,-42,-44,-47,-52,-55,-59,-62,-69,-70,-71,-60,-68,-61,-41,-66,-43,-45,-46,-48,-49,-50,-51,-53,-54,-56,-57,-58,-72,-67,-65,-67,]),'MULTIPLICACAO':([50,55,57,58,61,62,63,96,97,98,117,126,127,128,129,130,132,143,144,155,],[-68,93,-59,-62,-69,-70,-71,-60,-68,-61,-66,93,93,-56,-57,-58,-72,-67,-65,-67,]),'DIVIDE':([50,55,57,58,61,62,63,96,97,98,117,126,127,128,129,130,132,143,144,155,],[-68,94,-59,-62,-69,-70,-71,-60,-68,-61,-66,94,94,-56,-57,-58,-72,-67,-65,-67,]),'MOD':([50,55,57,58,61,62,63,96,97,98,117,126,127,128,129,130,132,143,144,155,],[-68,95,-59,-62,-69,-70,-71,-60,-68,-61,-66,95,95,-56,-57,-58,-72,-67,-65,-67,]),'MAIS':([50,54,55,57,58,61,62,63,96,97,98,117,122,123,124,125,126,127,128,129,130,132,143,144,155,],[-68,91,-55,-59,-62,-69,-70,-71,-60,-68,-61,-66,91,91,91,91,-53,-54,-56,-57,-58,-72,-67,-65,-67,]),'MENOR':([50,53,54,55,57,58,61,62,63,96,97,98,117,120,121,122,123,124,125,126,127,128,129,130,132,143,144,155,],[-68,87,-52,-55,-59,-62,-69,-70,-71,-60,-68,-61,-66,87,87,-48,-49,-50,-51,-53,-54,-56,-57,-58,-72,-67,-65,-67,]),'MAIOR':([50,53,54,55,57,58,61,62,63,96,97,98,117,120,121,122,123,124,125,126,127,128,129,130,132,143,144,155,],[-68,88,-52,-55,-59,-62,-69,-70,-71,-60,-68,-61,-66,88,88,-48,-49,-50,-51,-53,-54,-56,-57,-58,-72,-67,-65,-67,]),'MAIORIGUAL':([50,53,54,55,57,58,61,62,63,96,97,98,117,120,121,122,123,124,125,126,127,128,129,130,132,143,144,155,],[-68,89,-52,-55,-59,-62,-69,-70,-71,-60,-68,-61,-66,89,89,-48,-49,-50,-51,-53,-54,-56,-57,-58,-72,-67,-65,-67,]),'MENORIGUAL':([50,53,54,55,57,58,61,62,63,96,97,98,117,120,121,122,123,124,125,126,127,128,129,130,132,143,144,155,],[-68,90,-52,-55,-59,-62,-69,-70,-71,-60,-68,-61,-66,90,90,-48,-49,-50,-51,-53,-54,-56,-57,-58,-72,-67,-65,-67,]),'ATRIBUICAO':([50,52,53,54,55,57,58,61,62,63,96,97,98,117,119,120,121,122,123,124,125,126,127,128,129,130,132,143,144,155,],[-68,85,-47,-52,-55,-59,-62,-69,-70,-71,-60,-68,-61,-66,85,-45,-46,-48,-49,-50,-51,-53,-54,-56,-57,-58,-72,-67,-65,-67,]),'DIFERENTE':([50,52,53,54,55,57,58,61,62,63,96,97,98,117,119,120,121,122,123,124,125,126,127,128,129,130,132,143,144,155,],[-68,86,-47,-52,-55,-59,-62,-69,-70,-71,-60,-68,-61,-66,86,-45,-46,-48,-49,-50,-51,-53,-54,-56,-57,-58,-72,-67,-65,-67,]),'E':([50,51,52,53,54,55,57,58,61,62,63,96,97,98,114,117,119,120,121,122,123,124,125,126,127,128,129,130,132,143,144,155,],[-68,84,-44,-47,-52,-55,-59,-62,-69,-70,-71,-60,-68,-61,84,-66,-43,-45,-46,-48,-49,-50,-51,-53,-54,-56,-57,-58,-72,-67,-65,-67,]),'NORMALSTRING':([67,],[103,]),'ENTAO':([135,],[149,]),'EXECUTE':([136,],[150,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Programa':([0,],[1,]),'DeclFuncVar':([0,13,18,108,],[2,20,37,139,]),'Tipo':([0,10,13,15,18,77,106,108,141,158,],[3,17,3,24,3,24,17,3,24,17,]),'DeclProg':([2,],[6,]),'Bloco':([7,16,27,41,149,150,159,],[9,35,35,75,35,35,35,]),'DeclVar':([8,21,36,38,109,138,],[11,39,71,73,140,151,]),'DeclFunc':([8,],[13,]),'ListaDeclVar':([10,106,158,],[16,137,160,]),'ListaParametros':([15,],[22,]),'ListaParametrosCont':([15,77,141,],[23,111,152,]),'ListaComando':([16,27,],[25,44,]),'Comando':([16,27,149,150,159,],[27,27,156,157,161,]),'Expr':([29,31,60,69,70,80,82,101,131,],[45,66,99,104,105,113,115,133,146,]),'AssignExpr':([29,31,60,69,70,79,80,82,83,101,131,145,],[46,46,46,46,46,112,46,46,118,46,46,154,]),'CondExpr':([29,31,60,69,70,79,80,82,83,101,131,142,145,],[47,47,47,47,47,47,47,47,47,47,47,153,47,]),'LValueExpr':([29,30,31,60,69,70,79,80,82,83,101,131,145,],[48,64,48,48,48,48,48,48,48,48,48,48,48,]),'OrExpr':([29,31,60,69,70,79,80,82,83,101,131,142,145,],[49,49,49,49,49,49,49,49,49,49,49,49,49,]),'AndExpr':([29,31,60,69,70,79,80,81,82,83,101,131,142,145,],[51,51,51,51,51,51,51,114,51,51,51,51,51,51,]),'EqExpr':([29,31,60,69,70,79,80,81,82,83,84,101,131,142,145,],[52,52,52,52,52,52,52,52,52,52,119,52,52,52,52,]),'DesigExpr':([29,31,60,69,70,79,80,81,82,83,84,85,86,101,131,142,145,],[53,53,53,53,53,53,53,53,53,53,53,120,121,53,53,53,53,]),'AddExpr':([29,31,60,69,70,79,80,81,82,83,84,85,86,87,88,89,90,101,131,142,145,],[54,54,54,54,54,54,54,54,54,54,54,54,54,122,123,124,125,54,54,54,54,]),'MulExpr':([29,31,60,69,70,79,80,81,82,83,84,85,86,87,88,89,90,91,92,101,131,142,145,],[55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,126,127,55,55,55,55,]),'UnExpr':([29,31,60,69,70,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,101,131,142,145,],[57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,128,129,130,57,57,57,57,]),'PrimExpr':([29,31,56,59,60,69,70,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,101,131,142,145,],[58,58,96,98,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,]),'ListExpr':([83,],[116,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Programa","S'",1,None,None,None),
  ('Programa -> DeclFuncVar DeclProg','Programa',2,'p_Programa','ply_syntax.py',22),
  ('DeclFuncVar -> Tipo NOME DeclVar PVIRGULA DeclFuncVar','DeclFuncVar',5,'p_DeclFuncVar','ply_syntax.py',26),
  ('DeclFuncVar -> Tipo NOME ECOCHETE INT DCOCHETE DeclVar PVIRGULA DeclFuncVar','DeclFuncVar',8,'p_DeclFuncVar','ply_syntax.py',27),
  ('DeclFuncVar -> Tipo NOME DeclFunc DeclFuncVar','DeclFuncVar',4,'p_DeclFuncVar','ply_syntax.py',28),
  ('DeclFuncVar -> <empty>','DeclFuncVar',0,'p_DeclFuncVar','ply_syntax.py',29),
  ('DeclProg -> PROGRAMA Bloco','DeclProg',2,'p_DeclProg','ply_syntax.py',33),
  ('DeclVar -> VIRGULA NOME DeclVar','DeclVar',3,'p_DeclVar','ply_syntax.py',37),
  ('DeclVar -> VIRGULA NOME ECOCHETE INT DCOCHETE DeclVar','DeclVar',6,'p_DeclVar','ply_syntax.py',38),
  ('DeclVar -> <empty>','DeclVar',0,'p_DeclVar','ply_syntax.py',39),
  ('DeclFunc -> EPAREN ListaParametros DPAREN Bloco','DeclFunc',4,'p_DeclFunc','ply_syntax.py',43),
  ('ListaParametros -> <empty>','ListaParametros',0,'p_ListaParametros','ply_syntax.py',47),
  ('ListaParametros -> ListaParametrosCont','ListaParametros',1,'p_ListaParametros','ply_syntax.py',48),
  ('ListaParametrosCont -> Tipo NOME','ListaParametrosCont',2,'p_ListaParametrosCont','ply_syntax.py',52),
  ('ListaParametrosCont -> Tipo NOME ECOCHETE DCOCHETE','ListaParametrosCont',4,'p_ListaParametrosCont','ply_syntax.py',53),
  ('ListaParametrosCont -> Tipo NOME VIRGULA ListaParametrosCont','ListaParametrosCont',4,'p_ListaParametrosCont','ply_syntax.py',54),
  ('ListaParametrosCont -> Tipo NOME ECOCHETE DCOCHETE VIRGULA ListaParametrosCont','ListaParametrosCont',6,'p_ListaParametrosCont','ply_syntax.py',55),
  ('Bloco -> ECHAVES ListaDeclVar ListaComando DCHAVES','Bloco',4,'p_Bloco','ply_syntax.py',59),
  ('Bloco -> ECHAVES ListaDeclVar DCHAVES','Bloco',3,'p_Bloco','ply_syntax.py',60),
  ('ListaDeclVar -> <empty>','ListaDeclVar',0,'p_ListaDeclVar','ply_syntax.py',64),
  ('ListaDeclVar -> Tipo NOME DeclVar PVIRGULA ListaDeclVar','ListaDeclVar',5,'p_ListaDeclVar','ply_syntax.py',65),
  ('ListaDeclVar -> Tipo NOME ECOCHETE INT DCOCHETE DeclVar PVIRGULA ListaDeclVar','ListaDeclVar',8,'p_ListaDeclVar','ply_syntax.py',66),
  ('Tipo -> INT','Tipo',1,'p_Tipo','ply_syntax.py',70),
  ('Tipo -> CAR','Tipo',1,'p_Tipo','ply_syntax.py',71),
  ('ListaComando -> Comando','ListaComando',1,'p_ListaComando','ply_syntax.py',75),
  ('ListaComando -> Comando ListaComando','ListaComando',2,'p_ListaComando','ply_syntax.py',76),
  ('Comando -> PVIRGULA','Comando',1,'p_Comando','ply_syntax.py',80),
  ('Comando -> RETORNE Expr PVIRGULA','Comando',3,'p_Comando','ply_syntax.py',81),
  ('Comando -> LEIA LValueExpr PVIRGULA','Comando',3,'p_Comando','ply_syntax.py',82),
  ('Comando -> ESCREVA Expr PVIRGULA','Comando',3,'p_Comando','ply_syntax.py',83),
  ('Comando -> ESCREVA ASPASD NORMALSTRING ASPASD PVIRGULA','Comando',5,'p_Comando','ply_syntax.py',84),
  ('Comando -> NOVALINHA PVIRGULA','Comando',2,'p_Comando','ply_syntax.py',85),
  ('Comando -> SE EPAREN Expr DPAREN ENTAO Comando','Comando',6,'p_Comando','ply_syntax.py',86),
  ('Comando -> SE EPAREN Expr DPAREN ENTAO Comando SENAO Comando','Comando',8,'p_Comando','ply_syntax.py',87),
  ('Comando -> ENQUANTO EPAREN Expr DPAREN EXECUTE Comando','Comando',6,'p_Comando','ply_syntax.py',88),
  ('Comando -> Bloco','Comando',1,'p_Comando','ply_syntax.py',89),
  ('Expr -> AssignExpr','Expr',1,'p_Expr','ply_syntax.py',93),
  ('AssignExpr -> CondExpr','AssignExpr',1,'p_AssignExpr','ply_syntax.py',97),
  ('AssignExpr -> LValueExpr IGUAL AssignExpr','AssignExpr',3,'p_AssignExpr','ply_syntax.py',98),
  ('CondExpr -> OrExpr','CondExpr',1,'p_CondExpr','ply_syntax.py',102),
  ('CondExpr -> OrExpr INTERROGACAO Expr DOISP CondExpr','CondExpr',5,'p_CondExpr','ply_syntax.py',103),
  ('OrExpr -> OrExpr OU AndExpr','OrExpr',3,'p_OrExpr','ply_syntax.py',107),
  ('OrExpr -> AndExpr','OrExpr',1,'p_OrExpr','ply_syntax.py',108),
  ('AndExpr -> AndExpr E EqExpr','AndExpr',3,'p_AndExpr','ply_syntax.py',112),
  ('AndExpr -> EqExpr','AndExpr',1,'p_AndExpr','ply_syntax.py',113),
  ('EqExpr -> EqExpr ATRIBUICAO DesigExpr','EqExpr',3,'p_EqExpr','ply_syntax.py',117),
  ('EqExpr -> EqExpr DIFERENTE DesigExpr','EqExpr',3,'p_EqExpr','ply_syntax.py',118),
  ('EqExpr -> DesigExpr','EqExpr',1,'p_EqExpr','ply_syntax.py',119),
  ('DesigExpr -> DesigExpr MENOR AddExpr','DesigExpr',3,'p_DesigExpr','ply_syntax.py',123),
  ('DesigExpr -> DesigExpr MAIOR AddExpr','DesigExpr',3,'p_DesigExpr','ply_syntax.py',124),
  ('DesigExpr -> DesigExpr MAIORIGUAL AddExpr','DesigExpr',3,'p_DesigExpr','ply_syntax.py',125),
  ('DesigExpr -> DesigExpr MENORIGUAL AddExpr','DesigExpr',3,'p_DesigExpr','ply_syntax.py',126),
  ('DesigExpr -> AddExpr','DesigExpr',1,'p_DesigExpr','ply_syntax.py',127),
  ('AddExpr -> AddExpr MAIS MulExpr','AddExpr',3,'p_AddExpr','ply_syntax.py',131),
  ('AddExpr -> AddExpr MENOS MulExpr','AddExpr',3,'p_AddExpr','ply_syntax.py',132),
  ('AddExpr -> MulExpr','AddExpr',1,'p_AddExpr','ply_syntax.py',133),
  ('MulExpr -> MulExpr MULTIPLICACAO UnExpr','MulExpr',3,'p_MulExpr','ply_syntax.py',137),
  ('MulExpr -> MulExpr DIVIDE UnExpr','MulExpr',3,'p_MulExpr','ply_syntax.py',138),
  ('MulExpr -> MulExpr MOD UnExpr','MulExpr',3,'p_MulExpr','ply_syntax.py',139),
  ('MulExpr -> UnExpr','MulExpr',1,'p_MulExpr','ply_syntax.py',140),
  ('UnExpr -> MENOS PrimExpr','UnExpr',2,'p_UnExpr','ply_syntax.py',144),
  ('UnExpr -> EXCLAMACAO PrimExpr','UnExpr',2,'p_UnExpr','ply_syntax.py',145),
  ('UnExpr -> PrimExpr','UnExpr',1,'p_UnExpr','ply_syntax.py',146),
  ('LValueExpr -> NOME ECOCHETE Expr DCOCHETE','LValueExpr',4,'p_LValueExpr','ply_syntax.py',150),
  ('LValueExpr -> NOME','LValueExpr',1,'p_LValueExpr','ply_syntax.py',151),
  ('PrimExpr -> NOME EPAREN ListExpr DPAREN','PrimExpr',4,'p_PrimExpr','ply_syntax.py',155),
  ('PrimExpr -> NOME EPAREN DPAREN','PrimExpr',3,'p_PrimExpr','ply_syntax.py',156),
  ('PrimExpr -> NOME ECOCHETE Expr DCOCHETE','PrimExpr',4,'p_PrimExpr','ply_syntax.py',157),
  ('PrimExpr -> NOME','PrimExpr',1,'p_PrimExpr','ply_syntax.py',158),
  ('PrimExpr -> NUMERO','PrimExpr',1,'p_PrimExpr','ply_syntax.py',159),
  ('PrimExpr -> CAR','PrimExpr',1,'p_PrimExpr','ply_syntax.py',160),
  ('PrimExpr -> INT','PrimExpr',1,'p_PrimExpr','ply_syntax.py',161),
  ('PrimExpr -> EPAREN Expr DPAREN','PrimExpr',3,'p_PrimExpr','ply_syntax.py',162),
  ('ListExpr -> AssignExpr','ListExpr',1,'p_ListExpr','ply_syntax.py',166),
  ('ListExpr -> ListExpr VIRGULA AssignExpr','ListExpr',3,'p_ListExpr','ply_syntax.py',167),
]
