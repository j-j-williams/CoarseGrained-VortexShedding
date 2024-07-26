###########################################################################
# This code is slightly adjusted from Zachary G. Nicolaou's code for computing the normal form parameters
# See: https://github.com/dynamicslab/pysindy/blob/master/examples/17_parameterized_pattern_formation/utils.py
# Specifically, on line 1280 of that code: def get_normal_form_parameters(model, us, printcoefs=False): 

# The changes are specifically to the computation of:  b ,  c ,  alpha 
###########################################################################


import numpy as np


def fnc_Compute_NormalFormParameters(lib, opt):


    ###  Compute the  Hopf bifurcation  normal form parameters  (beta, sigma)


    # lib = model.feature_library
    # opt = model.optimizer


    bs = np.linspace(0, 1, 1)


    # D = np.zeros((len(bs), 2, 2))
    # D[:, :, 0] = opt.coef_[:, 11].T
    # D[:, :, 1] = opt.coef_[:, 12].T


    A = np.zeros((len(bs), 2, 2))
    A[:, :, 0] = [1, 0] # - opt.coef_[:, Xts].T
    A[:, :, 1] = [0, 1] # - opt.coef_[:, Yts].T



    J = np.zeros((len(bs), 2, 2))
    Fxx = np.zeros((len(bs), 2, 2, 2))
    Fxxx = np.zeros((len(bs), 2, 2, 2, 2))


    J[:, :, 0] = opt.coef_[:, 0].T
    J[:, :, 1] = opt.coef_[:, 1].T
    Fxx[:, :, 0, 0] = opt.coef_[:, 2].T * 2
    Fxx[:, :, 0, 1] = opt.coef_[:, 4].T
    Fxx[:, :, 1, 0] = opt.coef_[:, 4].T
    Fxx[:, :, 1, 1] = opt.coef_[:, 3].T * 2
    Fxxx[:, :, 0, 0, 0] = opt.coef_[:, 5].T * 6
    Fxxx[:, :, 0, 0, 1] = opt.coef_[:, 7].T * 2
    Fxxx[:, :, 0, 1, 0] = opt.coef_[:, 7].T * 2
    Fxxx[:, :, 1, 0, 0] = opt.coef_[:, 7].T * 2
    Fxxx[:, :, 0, 1, 1] = opt.coef_[:, 8].T * 2
    Fxxx[:, :, 1, 0, 1] = opt.coef_[:, 8].T * 2
    Fxxx[:, :, 1, 1, 0] = opt.coef_[:, 8].T * 2
    Fxxx[:, :, 1, 1, 1] = opt.coef_[:, 6].T * 6

    lambdas, Us = np.linalg.eig(np.einsum("aij,ajk->aik", np.linalg.inv(A), J))

    u_rename = Us[:, :, 0]
    ubar_rename = np.conjugate(u_rename)
    ut_rename = np.linalg.inv(Us)[:, 0, :]

    a = np.einsum(
        "ni,nip,npjk,nj,nkl,nlmo,nm,no->n",
        ut_rename,
        np.linalg.inv(A),
        Fxx,
        u_rename,
        np.linalg.inv(J),
        Fxx,
        u_rename,
        ubar_rename,
    )

    b = (
        np.einsum(
            "ni,nip,npjk,nj,nkl,nlmo,nm,no->n",
            ut_rename,
            np.linalg.inv(A),
            Fxx,
            ubar_rename,
            np.linalg.inv(
                -J
                + (
                    2*(lambdas[:, 0] - lambdas[:, 1])[:, np.newaxis, np.newaxis]
                    * np.eye(2)[np.newaxis, :, :]
                )
            ),
            Fxx,
            u_rename,
            u_rename,
        )
        / 1
    )

    c = (
        np.einsum("ni,nip,npjkl,nj,nk,nl->n", ut_rename, np.linalg.inv(A), Fxxx, u_rename, u_rename, ubar_rename)
        / 1
    )



    ###  Compute  alpha
    #  This is the way to determine the parameters from Kuznetsov

    alphas = c - 2*a + b
    ANS_a_2 = np.real(alphas)

    # alphas = a + b - c
    # ANS_a, ANS_b = -np.imag(alphas) / np.real(alphas), np.imag(betas) / np.real(betas)

    print('\nValue of ANS_a  =  ' + str(ANS_a_2)+'\n\n')



    # betas = np.einsum("ni,nij,njk,nk->n", ut_rename, np.linalg.inv(A), D, u_rename)

    Beta_hopf_1 = opt.coef_.T[0,0] / ( -1* opt.coef_.T[1,0] )
    Beta_hopf_2 = opt.coef_.T[1,1] / opt.coef_.T[0,1]
    Beta_hopf_avg = np.mean([Beta_hopf_1,Beta_hopf_2])

    print('( 1st , 2nd )  Value of Beta  =  ( ' + str(Beta_hopf_1) + ' , ' + str(Beta_hopf_2) + ' )')
    print('\nAvg Value of Beta  =  ' + str(Beta_hopf_avg ) )

    print('\n\n')


    return ANS_a_2, Beta_hopf_avg

